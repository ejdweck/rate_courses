from django.conf.urls import url
from django.contrib.auth import views as auth_views
from django.contrib import admin
from . import views
from course import views as core_views

urlpatterns = [
    # template urls
    url(r'^$', views.homepage, name='homepage'),
    url(r'^about/$', views.about, name='about'),
 	url(r'^courses/$', views.courses, name='courses'),
    url(r'^course_reviews/$', views.course_reviews, name='course_reviews'),
    url(r'^add_course_review/$', views.add_course_review, name='add_course_review'),
    url(r'^search/$', views.search, name='search'),

    # authentification system urls
    url(r'^login/$', auth_views.login, name='login'),
    url(r'^logout/$', auth_views.logout, name='logout'),
    url(r'^signup/$', core_views.signup, name='signup'),

    # admin page url
    url(r'^admin/', admin.site.urls),
    ]
