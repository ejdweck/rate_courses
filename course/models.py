from django.db import models

class Instructor(models.Model):
	instructorId = models.AutoField(primary_key=True)
	firstName = models.CharField(max_length=20)
	lastName = models.CharField(max_length=20)

class GradeDistributionData(models.Model):
	gradeDistributionDataId = models.AutoField(primary_key=True)
	numberGrades = models.CharField(max_length=5)
	averageGpa = models.CharField(max_length=5) 
	a = models.CharField(max_length=5)
	ab = models.CharField(max_length=5)
	b = models.CharField(max_length=5) 
	bc = models.CharField(max_length=5)
	c = models.CharField(max_length=5)
	d = models.CharField(max_length=5)
	f = models.CharField(max_length=5)
	s = models.CharField(max_length=5)
	u = models.CharField(max_length=5)
	cr = models.CharField(max_length=5)
	n = models.CharField(max_length=5)
	p = models.CharField(max_length=5)
	i = models.CharField(max_length=5)
	nw = models.CharField(max_length=5)
	nr = models.CharField(max_length=5)
	o = models.CharField(max_length=5)
	'''
	numberGrades = models.IntegerField()
	averageGpa = models.DecimalField(max_digits=5, decimal_places=5) 
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
	'''
class GradeDistributionSemester(models.Model):
	gradeDistributionSemesterId = models.AutoField(primary_key=True)
	fall15 = models.ForeignKey(GradeDistributionData, related_name='fall15', on_delete = models.CASCADE)
	spring15 = models.ForeignKey(GradeDistributionData, related_name='spring15', on_delete = models.CASCADE)
	fall16 = models.ForeignKey(GradeDistributionData, related_name='fall16', on_delete = models.CASCADE)
	spring16 = models.ForeignKey(GradeDistributionData, related_name='spring16', on_delete = models.CASCADE)
	fall17 = models.ForeignKey(GradeDistributionData, related_name='fall17', on_delete = models.CASCADE)
	spring17 = models.ForeignKey(GradeDistributionData, related_name='spring17', on_delete = models.CASCADE)
	fall18 = models.ForeignKey(GradeDistributionData, related_name='fall18', on_delete = models.CASCADE)
	spring18 = models.ForeignKey(GradeDistributionData, related_name='spring18', on_delete = models.CASCADE)

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
