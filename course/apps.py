from django.apps import AppConfig
from watson import search as watson

class CourseConfig(AppConfig):
    name = 'course'
    def ready(self):
        Course = self.get_model('Course')
        CourseReview = self.get_model('CourseReview')
        Instructor = self.get_model('Instructor')
        watson.register(Course, exclude = ('averageRating', 'numberOfRatings'))
        watson.register(CourseReview, exclude=('reviewId', 'instructorId', 'courseReviewTagId', 'review', 'rating', 'reviewDate'))
        watson.register(Instructor, exclude=('instructorId'))  
