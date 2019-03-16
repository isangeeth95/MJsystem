from django import forms
from .models import *

class add_ItemForm(forms.ModelForm):
    class Meta:
        model = jewelry
        fields= ('category','slug', 'date', 'description', 'charges', 'stoneType' , 'NoOfStones', 'weight', 'quantity', 'craftsman_id', 'status', 'issues', 'image')

class edit_ItemForm(forms.ModelForm):
    class Meta:
        model = jewelry
        fields= ('category','slug', 'date', 'description', 'charges', 'stoneType' , 'NoOfStones', 'weight', 'quantity', 'craftsman_id', 'status', 'issues', 'image')
