from django import forms
from .models import *

class add_craftsmenForm(forms.ModelForm):
    class Meta:
        model = craftsmen
        fields = ('first_Name', 'last_Name', 'nic', 'address', 'phone_No','craftsmen_Item')

class edit_craftsmen(forms.ModelForm):
    class Meta:
        model = craftsmen
        fields = ('first_Name', 'last_Name', 'nic', 'address', 'phone_No', 'craftsmen_Item')