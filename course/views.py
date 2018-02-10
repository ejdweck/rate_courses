from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.db import connection
from course.forms import AddCourseReviewForm
from course.models import CourseReview, Course, Instructor, CourseReviewTag, GradeDistributionData
from django.db.models import Avg
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from watson import search as watson
import datetime
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import get_object_or_404 

search_query = ""

def homepage(request):
    # get course review objects for rendering on the homepage
    #course_reviews_list = CourseReview.objects.all().order_by('reviewDate')
    course_list = Course.objects.all()

    # get page objects
    courses = create_pages_object_limit_6(request, course_list)
   
    # list including necessary data for html blog tags (form, courses, instructurs, course_reviews)
    argumentList = modal_form(request)
    return render(request, 'homepage.html', {'form':argumentList[0],'courses':courses,'instructors':argumentList[2]})

def about(request):
    # list including necessary data for html block tags (form, courses, instructurs, course_reviews)
    argumentList = modal_form(request)
    return render(request, 'about.html', {'form':argumentList[0],'courses':argumentList[1],'instructors':argumentList[2]})

def course_detail(request, pk):
    # get course object to render a page for
    course = get_object_or_404(Course, pk=pk)

    course_department = course.courseDepartment
    course_number = course.courseNumber

    course_reviews = CourseReview.objects.filter(courseId=course)
    course_reviews_pages = create_pages_object_limit_4(request, course_reviews)

    argumentList = modal_form(request)

    return render(request, 'course_detail.html', {'course': course,'course_reviews':course_reviews_pages, 'form':argumentList[0]})

def search(request):
    argumentList = modal_form(request)
    if request.method == 'GET': # If the form is submitted
        search_query = request.GET.get('searchbox')
        # search on Course table
        if search_query is not None:
            courses = watson.filter(Course, search_query)
            # create page objects with orginal query
            courses_pages = create_pages_object_limit_6(request, courses)
            return render(request, 'search.html', {'courses': courses_pages, 'form': argumentList[0]})
        else:
            courses = Course.objects.all()
            courses_pages = create_pages_object_limit_6(request, courses)
            argumentList = modal_form(request)
            print(search_query)
            return render(request, 'search.html', {'courses': courses_pages, 'form': argumentList[0]})

    elif request.method == 'POST':
        courses = Course.objects.all()
        course_pages = create_pages_object_limit_6(request, courses)
        argumentList = modal_form(request)

        return render(request, 'search.html', {'courses': course_pages, 'form': argumentList[0]})


def create_pages_object_limit_6(request, objectList):
    page = request.GET.get('page', 1)
    paginator = Paginator(objectList, 6)
    try:
        objects = paginator.page(page)
    except PageNotAnInteger:
        objects = paginator.page(1)
    except EmptyPage:
        print("EMPTY PAGE FUCK")
        objects = paginator.page(paginator.num_pages)
    return objects

def create_pages_object_limit_4(request, objectList):
    page = request.GET.get('page', 1)
    paginator = Paginator(objectList, 4)
    try:
        objects = paginator.page(page)
    except PageNotAnInteger:
        objects = paginator.page(1)
    except EmptyPage:
        print("EMPTY PAGE FUCK")
        objects = paginator.page(paginator.num_pages)
    return objects

def modal_form(request):
    if request.method == 'GET':
        form = AddCourseReviewForm(auto_id=True)
        # get courses for auto complete
        courses = Course.objects.all()
        # get instructors names for auto complete
        instructors = Instructor.objects.all()
        argumentList = [form, courses, instructors]
        return argumentList # 'courses': courses, 'instructors': instructors})
    else:
        form = AddCourseReviewForm(request.POST,auto_id=True)
        # get courses for auto complete
        courses = Course.objects.all()
        # get instructors names for auto complete
        instructors = Instructor.objects.all()
        argumentList = [form, courses, instructors]
        if form.is_valid():
            # parse course department and course number from single field on form
            courseDepartmentIndex = 0
            courseDepartmentAndNumber = form.cleaned_data['courseDepartmentAndNumber']
            for c in range(len(courseDepartmentAndNumber)):
                if (courseDepartmentAndNumber[c].isdigit()):
                    courseDepartmentIndex = c
                    break;

            courseDepartment = courseDepartmentAndNumber[0:courseDepartmentIndex]
            # force courseDepartment to uppercase letters for consistency in database
            courseDepartment = courseDepartment.upper()
            courseNumber = courseDepartmentAndNumber[courseDepartmentIndex:len(courseDepartmentAndNumber)]
            # parse review from form on field
            review = form.cleaned_data['review']
            # parse rating from form on field
            rating = form.cleaned_data['rating']
            # determine if weed out button has been pressed on form on field
            weedOutButton = form.cleaned_data['weedOutCourse']
            interestingContent = form.cleaned_data['interestingContent']
            lotsOfHomework = form.cleaned_data['lotsOfHomework']
            mandatoryAttendance = form.cleaned_data['mandatoryAttendance']
            # create CourseReviewTags object
            courseReviewTag = CourseReviewTag.objects.create(weedOutCourse=weedOutButton, interestingContent=interestingContent, lotsOfHomework=lotsOfHomework, mandatoryAttendance=mandatoryAttendance) 
            # set the review date to the current day
            reviewDate = datetime.datetime.today()
            # parse instructor first name and last name into individual fields
            instructorName = form.cleaned_data['instructorName']
            names = instructorName.split()
            instructorFirstName = "" 
            instructorLastName = ""
            if (len(names) >= 2):
                instructorFirstName = names[0]
                instructorLastName = names[1]

            avgRating = 0.0
            numRatings = 0
            # check if course already exists in database by querying
            try:
                course = Course.objects.filter(courseDepartment=courseDepartment,courseNumber=courseNumber).get()
            except ObjectDoesNotExist:
                course = None
                print("course review not added because course not in database")
                return argumentList;

            # instructor object to pass into course review as we linked the models via Foreign Keys
            instructorObject = ""
            try:
                # find out if we need to create a new instructor
                instructor = Instructor.objects.get(firstName=instructorFirstName,lastName=instructorLastName)
                instructorObject = instructor
            except ObjectDoesNotExist:
                # add new instructor 
                newInstructor = Instructor.objects.create(
                    firstName=instructorFirstName,
                    lastName=instructorLastName
                    )
                instructorId = newInstructor.instructorId
                instructorObject = newInstructor

            # if course exists, just add course on the id of the instructor from instructor table
            courseReview = CourseReview.objects.create(
                courseId = course,
                instructorId = instructorObject,
                courseReviewTagId = courseReviewTag,
                review = review,
                rating = rating,
                reviewDate = reviewDate

            )
            # generate the course rating
            courseRatingAvg = CourseReview.objects.filter(courseId=course).aggregate(Avg('rating'))
            # update courses avg rating
            course = Course.objects.get(courseDepartment=course.courseDepartment,courseNumber=course.courseNumber)
            course.averageRating = courseRatingAvg['rating__avg']
            # update number of reviews by adding 1
            course.numberOfRatings += 1
            # commit the changes
            course.save()
            return argumentList
