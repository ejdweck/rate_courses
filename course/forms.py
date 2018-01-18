import datetime
from django import forms

class AddCourseReviewForm(forms.Form):
    courseDepartmentAndNumber = forms.CharField(
        required = True,
        label = 'courseDepartmentAndNumber',
        max_length = 32
    )
    '''
    courseDepartment = forms.CharField(
        required = True,
        label = 'courseDepartment',
        max_length = 32
    )
    courseNumber = forms.CharField(
        required = True,
        label = 'courseNumber',
        max_length = 32
    )
    '''

    instructorName = forms.CharField(
        required = True,
        label = 'instructorName',
        max_length = 32
    )
    '''
    instructorFirstName = forms.CharField(
        required = True,
        label = 'instructor first name',
        max_length = 32
    )
    instructorLastName = forms.CharField(
        required = True,
        label = 'instructor last name',
        max_length = 32
    )
    '''
    review = forms.CharField(
    	required = True,
    	label = 'review',
    	max_length = 32
    )
    rating = forms.IntegerField(
    	required = True,
    	label = 'rating',
        widget=forms.TextInput(attrs={'type': 'range','min':'0','max':'10','step':'1'})
    )
    '''
    reviewDate = forms.DateField(
    	initial = datetime.date.today
    )
    '''
