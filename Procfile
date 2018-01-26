web:python manage.py runserver
web: gunicorn rate_courses.wsgi --log-file -
heroku ps:scale web=1
