from django.conf.urls import url
from django.contrib.auth import views as auth_views
from django.contrib import admin
from . import views
from course import views as core_views

urlpatterns = [
    # template urls
    url(r'^$', views.homepage, name='homepage'),
    url(r'^about/$', views.about, name='about'),
    url(r'^search/$', views.search, name='search'),
    url(r'^course/(?P<pk>\d+)/$', views.course_detail, name='course_detail'),

    # admin page url
    url(r'^admin/', admin.site.urls),
    ]
