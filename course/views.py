from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.db import connection
from course.forms import AddCourseReviewForm
from course.models import CourseReview, Course, Instructor
from django.db.models import Avg
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from watson import search as watson
import datetime

def homepage(request):
    
    course_reviews = CourseReview.objects.all().order_by('reviewDate')[:3]
    return render(request, 'homepage.html', {'course_reviews': course_reviews})

def about(request):
    return render(request, 'about.html')

def courses(request):

    courses = Course.objects.all()
    return render(request, 'courses.html', {'courses':courses})

def course_reviews(request):
    course_reviews = CourseReview.objects.all().order_by('reviewDate')

    return render(request, 'course_reviews.html', {'course_reviews': course_reviews})

def add_course_review(request):
    if request.method == 'GET':
        form = AddCourseReviewForm(auto_id=True)
    else:
        form = AddCourseReviewForm(request.POST,auto_id=True)
        if form.is_valid():
            #courseDepartment = form.cleaned_data['courseDepartment']
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

            #courseNumber = form.cleaned_data['courseNumber']
            review = form.cleaned_data['review']
            rating = form.cleaned_data['rating']

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

                # get the userId for the user leaving the review
                currentUser = request.user
                currentUserId = currentUser.id

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
                    reviewerId = currentUserId,
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
                # get the userId for the user leaving the review
                currentUser = request.user
                currentUserId = currentUser.id

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
                    reviewerId = currentUserId,
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

            return render(request, "submission.html")
    # get courses for auto complete
    courses = Course.objects.all()
    # get instructors names for auto complete
    instructors = Instructor.objects.all()

    return render(request, "add_course_review_form.html", {'form': form, 'courses': courses, 'instructors': instructors})
    #return render(request, "add_course_review.html", {'form': form, 'courses': courses, 'instructors': instructors})

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            print("in signup")
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('homepage')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})

def search(request):
    if request.method == 'GET': # If the form is submitted
        
        search_query = request.GET.get('searchbox')
        courses = watson.filter(Course, search_query)
        course_reviews = watson.filter(CourseReview, search_query)
       
        for c in course_reviews:
            print(c.instructorId.lastName)
        
        print ("in search")
        print (courses)
        return render(request, 'search.html', {'courses':courses, 'course_reviews':course_reviews})
    # Your code
