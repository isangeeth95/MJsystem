from django import forms
from .models import *
from accounts.models import User

# class StaffForm1(forms.ModelForm):
#     class Meta:
#         model = Staff
#         fields = ('Emp_ID', 'First_Name','Last_Name', 'Email', 'Phone_Number', 'Admission_date', 'Job_title', 'Job_level')


class StaffForm(forms.Form):
    First_Name = forms.CharField(label='Full Name', widget=forms.TextInput(attrs={
                                                                        'class': 'form-control',
                                                                        'autofocus': 'autofocus',
                                                                    }))
    Last_Name = forms.CharField(label='Last Name', widget=forms.TextInput(attrs={
                                                                        'class': 'form-control',
                                                                        'autofocus': 'autofocus',
                                                                    }))
    Email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={
                                                                        'class': 'form-control',
                                                                        'autofocus': 'autofocus',
                                                                    }))
    NIC = forms.CharField(label='NIC', widget=forms.TextInput(attrs={
                                                                        'class': 'form-control',
                                                                        'autofocus': 'autofocus',
                                                                    }))
    Phone_Number = forms.IntegerField(label='Phone Number', widget=forms.TextInput(attrs={
                                                                        'class': 'form-control',
                                                                        'autofocus': 'autofocus',
                                                                    }))
    Job_title = forms.CharField(label='Job Title', widget=forms.TextInput(attrs={
                                                                        'class': 'form-control',
                                                                        'autofocus': 'autofocus',
                                                                    }))
    Job_level = forms.CharField(label='Job Level', widget=forms.TextInput(attrs={
                                                                        'class': 'form-control',
                                                                        'autofocus': 'autofocus',
                                                                    }))
    im = forms.BooleanField(label='Inventory',required=False)
    hrm = forms.BooleanField(label='HR Manage',required=False)  # hr manager
    dm = forms.BooleanField(label='delivery',required=False)  # delivery manager
    cm = forms.BooleanField(label='Customer Manage',required=False)  # customer manager
    sm = forms.BooleanField(label='Sales Manage',required=False)  # sales manager
    supm = forms.BooleanField(label='Supplier Manage',required=False)  # Supplier manager

    error = ' '

    def clean_email(self):
        email = self.cleaned_data.get('Email')
        qs = User.objects.filter(email=email)
        if qs.exists():
            self.error += "Email is taken"
            raise forms.ValidationError("Email is taken")
        return email