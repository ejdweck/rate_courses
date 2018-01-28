from django.apps import AppConfig
from watson import search as watson

class CourseConfig(AppConfig):
    name = 'course'
    def ready(self):
        Course = self.get_model('Course')
        watson.register(Course)
