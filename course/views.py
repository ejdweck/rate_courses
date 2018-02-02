from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.db import connection
from course.forms import AddCourseReviewForm
from course.models import CourseReview, Course, Instructor, CourseReviewTag
from django.db.models import Avg
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from watson import search as watson
import datetime
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def homepage(request):
    # get course review objects for rendering on the homepage
    #course_reviews_list = CourseReview.objects.all().order_by('reviewDate')
    course_review_list = CourseReview.objects.all()

    # get page objects
    course_reviews = create_pages_object(request, course_review_list)
   
    # list including necessary data for html blog tags (form, courses, instructurs, course_reviews)
    argumentList = modal_form(request)
    return render(request, 'homepage.html', {'form':argumentList[0],'courses':argumentList[1],'instructors':argumentList[2],'course_reviews':course_reviews})

def about(request):
    # list including necessary data for html block tags (form, courses, instructurs, course_reviews)
    argumentList = modal_form(request)
    return render(request, 'about.html', {'form':argumentList[0],'courses':argumentList[1],'instructors':argumentList[2]})

def courses(request):
    # list including necessary data for html block tags (form, courses, instructurs, course_reviews)
    argumentList = modal_form(request)
    return render(request, 'courses.html', {'form':argumentList[0],'courses':argumentList[1],'instructors':argumentList[2]})

def course_reviews(request):
    # list including necessary data for html block tags (form, courses, instructurs, course_reviews)
    argumentList = modal_form(request)
    course_reviews = CourseReview.objects.all().order_by('reviewDate')
    return render(request, 'course_reviews.html', {'form':argumentList[0],'courses':argumentList[1],'instructors':argumentList[2],'course_reviews':course_reviews})

def search(request):
    if request.method == 'GET': # If the form is submitted
        search_query = request.GET.get('searchbox')
        # search on Course table
        courses = watson.filter(Course, search_query)
        # search on CourseReview table
        course_reviews = watson.filter(CourseReview, search_query)
        print(course_reviews)
        for c in course_reviews:
            print(c.instructorId.lastName)
        return render(request, 'search.html', {'courses': courses, 'course_reviews': course_reviews})

def create_pages_object(request, objectList):
    page = request.GET.get('page', 1)
    paginator = Paginator(objectList, 6)
    try:
        objects = paginator.page(page)
    except PageNotAnInteger:
        objects = paginator.page(1)
    except EmptyPage:
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
        print(argumentList)
        return argumentList # 'courses': courses, 'instructors': instructors})
    else:
        form = AddCourseReviewForm(request.POST,auto_id=True)
        # get courses for auto complete
        courses = Course.objects.all()
        # get instructors names for auto complete
        instructors = Instructor.objects.all()
        argumentList = [form, courses, instructors]
        print(argumentList)
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
            course = Course.objects.filter(courseDepartment=courseDepartment,courseNumber=courseNumber)

            # if the course doesn't exist...
            if not course.count():
                # create course
                new_course = Course.objects.create(courseDepartment=courseDepartment,courseNumber=courseNumber,courseName='',averageRating=avgRating,numberOfRatings=numRatings)

                # instructor object to pass into course review as we linked the models via Foreign Keys
                instructorObject = ""

                try:
                    # find out if we need to create a new instructor
                    instructor = Instructor.objects.get(firstName=instructorFirstName,lastName=instructorLastName)
                    instructorObject = instructor
                except ObjectDoesNotExist:
                    # create Instructor tuple if new instructor
                    newInstructor = Instructor.objects.create(
                        firstName=instructorFirstName,
                        lastName=instructorLastName
                        )
                    instructorObject = newInstructor
                
                # add the course review
                courseReview = CourseReview.objects.create(
                    courseDepartment = courseDepartment,
                    courseNumber = courseNumber,
                    instructorId = instructorObject,
                    courseReviewTagId = courseReviewTag,
                    review = review,
                    rating = rating,
                    reviewDate = reviewDate 
                ) 

                # generate the course rating
                courseRatingAvg = CourseReview.objects.filter(courseDepartment=courseDepartment,courseNumber=courseNumber).aggregate(Avg('rating'))
                # update courses avg rating
                course = Course.objects.get(courseDepartment=courseDepartment,courseNumber=courseNumber)
                course.averageRating = courseRatingAvg['rating__avg']
                # update number of reviews by adding 1
                course.numberOfRatings += 1
                # commit the changes
                course.save()

            else:
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
                    courseDepartment = courseDepartment,
                    courseNumber = courseNumber,
                    instructorId = instructorObject,
                    courseReviewTagId = courseReviewTag,
                    review = review,
                    rating = rating,
                    reviewDate = reviewDate
                )

                # generate the course rating
                courseRatingAvg = CourseReview.objects.filter(courseDepartment=courseDepartment,courseNumber=courseNumber).aggregate(Avg('rating'))
                # update courses avg rating
                course = Course.objects.get(courseDepartment=courseDepartment,courseNumber=courseNumber)
                course.averageRating = courseRatingAvg['rating__avg']
                # update number of reviews by adding 1
                course.numberOfRatings += 1
                # commit the changes
                course.save()
            return argumentList
