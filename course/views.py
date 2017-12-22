from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.db import connection

def homepage(request):
    cursor = connection.cursor()
    query = 'SELECT Course.courseId, CourseReview.professor, CourseReview.review FROM Course, CourseReview WHERE Course.courseId = CourseReview.courseId'
    cursor.execute(query)
    reviews = cursor.fetchall()
    return render(request, 'homepage.html', {'reviews': reviews})


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('index')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})
