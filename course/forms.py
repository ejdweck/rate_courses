import datetime
from django import forms

class AddCourseReviewForm(forms.Form):
    courseDepartmentAndNumber = forms.CharField(
        required = True,
        label = 'courseDepartmentAndNumber',
        max_length = 32
    )

    instructorName = forms.CharField(
        required = True,
        label = 'instructorName',
        max_length = 32
    )

    rating = forms.IntegerField(
    	required = True,
    	label = 'rating',
        widget=forms.TextInput(attrs={'type': 'range','min':'0','max':'10','step':'1'})
    )

    weedOutCourse = forms.IntegerField(
        required = False,
        label = 'weedOutCourse',
        initial = 0,
        widget=forms.HiddenInput()
    )
   
    interestingContent = forms.IntegerField(
        required = False,
        label = 'interestingContent',
        initial = 0,
        widget=forms.HiddenInput()
    )

    lotsOfHomework = forms.IntegerField(
        required = False,
        label = 'lotsOfHomework',
        initial = 0,
        widget=forms.HiddenInput()
    )
  
    mandatoryAttendance = forms.IntegerField(
        required = False,
        label = 'mandatoryAttendance',
        initial = 0,
    )
 
    review = forms.CharField(
        required = True,
        label = 'review',
        max_length = 180 
    )