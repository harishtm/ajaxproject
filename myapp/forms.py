from django import forms
from myapp.models import *

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
