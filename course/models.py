from django.db import models

class Instructor(models.Model):
	instructorId = models.AutoField(primary_key=True)
	firstName = models.CharField(max_length=20)
	lastName = models.CharField(max_length=20)

class GradeDistributionData(models.Model):
	gradeDistributionDataId = models.AutoField(primary_key=True)
	numberGrades = models.IntegerField()
	averageGpa = models.DecimalField(max_digits=4, decimal_places=3) 
	a = models.DecimalField(max_digits=3, decimal_places=1)
	ab = models.DecimalField(max_digits=3, decimal_places=1)
	b = models.DecimalField(max_digits=3, decimal_places=1)
	bc = models.DecimalField(max_digits=3, decimal_places=1)
	c = models.DecimalField(max_digits=3, decimal_places=1)
	d = models.DecimalField(max_digits=3, decimal_places=1)
	f = models.DecimalField(max_digits=3, decimal_places=1)
	s = models.DecimalField(max_digits=3, decimal_places=1)
	u = models.DecimalField(max_digits=3, decimal_places=1)
	cr = models.DecimalField(max_digits=3, decimal_places=1)
	n = models.DecimalField(max_digits=3, decimal_places=1)
	p = models.DecimalField(max_digits=3, decimal_places=1)
	i = models.DecimalField(max_digits=3, decimal_places=1)
	nw = models.DecimalField(max_digits=3, decimal_places=1)
	nr = models.DecimalField(max_digits=3, decimal_places=1)
	o = models.DecimalField(max_digits=3, decimal_places=1)

class Course(models.Model):
	courseId = models.AutoField(primary_key=True)
	courseDepartment = models.CharField(max_length=3)
	courseNumber = models.CharField(max_length=3)
	courseName = models.CharField(max_length=50)
	averageRating = models.DecimalField(max_digits=3, decimal_places=1)
	numberOfRatings = models.IntegerField()
	credits = models.CharField(max_length=5)
	courseInfo = models.CharField(max_length=400)
	gradeDistributionDataId = models.ForeignKey(GradeDistributionData, on_delete = models.CASCADE)

class CourseReviewTag(models.Model):
	courseReviewTagId = models.AutoField(primary_key=True)
	weedOutCourse = models.IntegerField()
	interestingContent = models.IntegerField()
	lotsOfHomework = models.IntegerField()
	mandatoryAttendance = models.IntegerField()

class CourseTag(models.Model):
	courseTagId = models.AutoField(primary_key=True)
	weedOutCourse = models.IntegerField()
	interestingContent = models.IntegerField()
	lotsOfHomework = models.IntegerField()
	mandatoryAttendance = models.IntegerField()


class CourseReview(models.Model):
	reviewId = models.AutoField(primary_key=True)
	courseId = models.ForeignKey(Course, on_delete = models.CASCADE)
	instructorId = models.ForeignKey(Instructor, on_delete = models.CASCADE)
	courseReviewTagId = models.ForeignKey(CourseReviewTag, on_delete = models.CASCADE)
	review = models.CharField(max_length=50)
	rating = models.IntegerField()
	reviewDate = models.DateField()

	def rating_percentage(self):
	   	return self.rating * 10
