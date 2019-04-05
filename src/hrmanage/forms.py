from django import forms
from .models import *

class StaffForm(forms.ModelForm):
    class Meta:
        model = Staff
        fields = ('Emp_ID', 'First_Name',  'Email', 'Phone_Number', 'Admission_date', 'Job_title', 'Job_level')


