from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, ReadOnlyPasswordHashField
from .models import User, Online_Customer
from customer.models import Customer



# User = get_user_model()


class UserAdminCreationForm(forms.ModelForm):
    """A form for creating new users. Includes all the required
    fields, plus a repeated password."""
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('email',)

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords didn't match")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super(UserAdminCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class UserAdminChangeForm(forms.ModelForm):
    """A form for updating users. Includes all the fields on
    the user, but replaces the password field with admin's
    password hash display field.
    """
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = User
        fields = ('email', 'password', 'active','staff','admin','onlinecustomer')

    def clean_password(self):
        # Regardless of what the user provides, return the initial value.
        # This is done here, rather than on the field, because the
        # field does not have access to the initial value
        return self.initial["password"]



class LoginForm(forms.Form):
    email = forms.EmailField(label='Email', widget=forms.EmailInput(
                                                            attrs={
                                                                'class': 'form-control',
                                                                'autofocus': 'autofocus',
                                                            }
                                                    ))
    password = forms.CharField(widget=forms.PasswordInput(
                                                            attrs={
                                                                'class': 'form-control',
                                                                'autofocus': 'autofocus',
                                                            }
                                                    ))


class SignUpForm(forms.Form):
    fname = forms.CharField(label='Full Name', widget=forms.TextInput(attrs={
                                                                'class': 'form-control',
                                                                'autofocus': 'autofocus',
                                                            }))
    lname = forms.CharField(label='Last Name', widget=forms.TextInput(attrs={
                                                                'class': 'form-control',
                                                                'autofocus': 'autofocus',
                                                            }))
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={
                                                                'class': 'form-control',
                                                                'autofocus': 'autofocus',
                                                            }))
    pwd1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={
                                                                'class': 'form-control',
                                                                'autofocus': 'autofocus',
                                                            }))
    pwd2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput(attrs={
                                                                'class': 'form-control',
                                                                'autofocus': 'autofocus',
                                                            }))
    address = forms.CharField(label='Address', widget=forms.Textarea(attrs={
                                                                'class': 'form-control',
                                                                'autofocus': 'autofocus',
                                                                'style': 'padding-top: 2.375rem',
                                                            }))
    phone = forms.IntegerField(label='Phone Number', widget=forms.TextInput(attrs={
                                                                'class': 'form-control',
                                                                'autofocus': 'autofocus',



                                                            }))
    user_image = forms.ImageField(label='Upload your picture', widget=forms.FileInput(attrs={
                                                                'class': 'form-control',
                                                                'autofocus': 'autofocus',
                                                            }))

    error = ' '

    def clean(self):
        data = self.cleaned_data
        password1 = self.cleaned_data.get('pwd1')
        password2 = self.cleaned_data.get('pwd2')
        if password1 != password2:
            self.error += "Password didn't match "
            raise forms.ValidationError("Passwords didn't match")
        return data

    def clean_email(self):
        email = self.cleaned_data.get('email')
        qs = User.objects.filter(email=email)
        if qs.exists():
            self.error += "Email is taken"
            raise forms.ValidationError("Email is taken")
        return email


class EditProfile(forms.Form):

    fname = forms.CharField(label= 'First Name')
    lname = forms.CharField(label= ' Last Name')
    address = forms.CharField(label='Address',widget=forms.Textarea())
    phone = forms.IntegerField(label='Phone Number')


class deleteProfile(forms.Form):
    password = forms.CharField(widget=forms.PasswordInput())