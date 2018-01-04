from django import forms

class add_course_review_form(forms.Form):
    courseId = forms.CharField(
        required = True,
        label = 'course',
        max_length = 32
    )
    email = forms.CharField(
        required = True,
        label = 'Email',
        max_length = 32,
    )
    password = forms.CharField(
        required = True,
        label = 'Password',
        max_length = 32,
        widget = forms.PasswordInput()
    )


  reviewId INTEGER NOT NULL,
  courseId INTEGER NOT NULL,
  professorId INTEGER NOT NULL,
  reviewerId INTEGER NOT NULL,
  review VARCHAR(30) NOT NULL,
  rating INTEGER NOT NULL,
  reviewDate DATE NOT NULL,