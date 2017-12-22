from django.db import models

class Course (models.Model):
    courseId = models.AutoField(primary_key=True)
    courseName = models.CharField(max_length=50)
    courseNumber = models.CharField(max_length=50)

class CourseReview(models.Model):
    reviewId = models.AutoField(primary_key=True)
    courseId = models.ForeignKey(Course, on_delete=models.CASCADE)
    review = models.CharField(max_length=50)
    review_date = models.DateField()
    professor = models.CharField(max_length=50)
