from django.apps import AppConfig
from watson import search as watson

class CourseConfig(AppConfig):
    name = 'course'
    def ready(self):
        Course = self.get_model('Course')
        CourseReview = self.get_model('CourseReview')
        Instructor = self.get_model('Instructor')
        watson.register(Course)
        watson.register(CourseReview)
        watson.register(Instructor)  
