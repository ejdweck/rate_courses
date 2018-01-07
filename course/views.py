from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.db import connection
from course.forms import AddCourseReviewForm
from course.models import CourseReview, Course
from django.http import HttpResponse


def homepage(request):
    cursor = connection.cursor()
    #query = 'SELECT Course.courseNumber, Course.courseName, Instructor.firstName, Instructor.lastName, CourseReview.review FROM Course, Instructor, CourseReview WHERE Course.courseId = CourseReview.courseId AND Instructor.professorID = CourseReview.professorId'
    query = ''
    cursor.execute(query)
    reviews = cursor.fetchall()
    return render(request, 'homepage.html', {'reviews': reviews})

def about(request):
    return render(request, 'about.html')

def courses(request):
    cursor = connection.cursor()
    query = 'SELECT * FROM Course'
    cursor.execute(query)
    courses = cursor.fetchall()
    return render(request, 'courses.html', {'courses':courses})

def course_reviews(request):
    cursor = connection.cursor()
    #query = 'SELECT Course.courseNumber, Course.courseName, CourseReview.instructorId, CourseReview.review FROM Course, CourseReview WHERE Course.courseNumber = CourseReview.courseNumber'
    query = ''
    cursor.execute(query)
    tuples = cursor.fetchall()
    return render(request, 'course_reviews.html', {'allcourses': tuples})

def add_course_review(request):
    if request.method == 'GET':
        form = AddCourseReviewForm()
    else:
        form = AddCourseReviewForm(request.POST)
        if form.is_valid():
            #course = CourseReview.objects.create()
            course_review = CourseReview(
                courseDepartment = form.cleaned_data['courseDepartment'],
                courseNumber = form.cleaned_data['courseNumber'],
                instructorId = form.cleaned_data['instructor'],
                reviewId=1,
                reviewerId=1,
                review = form.cleaned_data['review'],
                rating = form.cleaned_data['rating'],
                reviewDate = form.cleaned_data['reviewDate']
            )
            course_review.save()

            return redirect('thanks')
    return render(request, "add_course_review.html", {'form': form})

def thanks(request):
    return HttpResponse('Thank you for your submission.')

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('homepage')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})
