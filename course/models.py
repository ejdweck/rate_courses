from django.db import models

class Instructor(models.Model):
	instructorId = models.AutoField(primary_key=True)
	firstName = models.CharField(max_length=20)
	lastName = models.CharField(max_length=20)

class Course(models.Model):
    courseDepartment = models.CharField(max_length=3)
    courseNumber = models.CharField(max_length=3)
    courseName = models.CharField(max_length=50)
    averageRating = models.DecimalField(max_digits=3, decimal_places=1)
    numberOfRatings = models.IntegerField()

    class Meta:
        unique_together = (('courseDepartment', 'courseNumber'),)

class GradePoint(models.Model):
	courseDepartment = models.CharField(max_length=3)
	courseNumber = models.CharField(max_length=3)
	fallSem15 = models.DecimalField(max_digits=3, decimal_places=1)
	springSem15 = models.DecimalField(max_digits=3, decimal_places=1)
	fallSem16 = models.DecimalField(max_digits=3, decimal_places=1)
	springSem16 = models.DecimalField(max_digits=3, decimal_places=1)
	fallSem17 = models.DecimalField(max_digits=3, decimal_places=1)
	springSem17 = models.DecimalField(max_digits=3, decimal_places=1)

	class Meta:
		unique_together = (('courseDepartment', 'courseNumber'),)

class CourseReview(models.Model):
	courseDepartment = models.CharField(max_length=3)
	courseNumber = models.CharField(max_length=3)
	reviewId = models.AutoField(primary_key=True)
	instructorId = models.IntegerField()
	reviewerId = models.IntegerField()
	review = models.CharField(max_length=50)
	rating = models.IntegerField()
	reviewDate = models.DateField()
