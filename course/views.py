from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.db import connection

def homepage(request):
    cursor = connection.cursor()
    query = 'SELECT Course.courseNumber, Course.courseName, CourseReview.professor, CourseReview.review FROM Course, CourseReview WHERE Course.courseId = CourseReview.courseId'
    cursor.execute(query)
    reviews = cursor.fetchall()
    return render(request, 'homepage.html', {'reviews': reviews})

def about(request):
    return render(request, 'about.html')

def courses(request):
    return render(request, 'courses.html')


def course_reviews(request):
    cursor = connection.cursor()
    query = 'SELECT Course.courseNumber, Course.courseName, CourseReview.professor, CourseReview.review FROM Course, CourseReview WHERE Course.courseId = CourseReview.courseId'
    cursor.execute(query)
    tuples = cursor.fetchall()
    return render(request, 'course_reviews.html', {'allcourses': tuples})


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
