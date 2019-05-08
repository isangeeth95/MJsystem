from django import forms
from .models import *

class add_ItemForm(forms.ModelForm):
    class Meta:
        model = jewelry
        fields= ('category', 'date', 'description', 'charges', 'stoneType' , 'NoOfStones', 'weight', 'quantity', 'craftsman_id', 'status', 'issues', 'image')



class edit_ItemForm(forms.ModelForm):
    class Meta:
        model = jewelry
        fields= ('category','date', 'description', 'charges', 'stoneType' , 'NoOfStones', 'weight', 'quantity', 'craftsman_id', 'status', 'issues', 'image')


class editGoldInfoForm(forms.ModelForm):
    class Meta:
        model = gold
        fields= ('code','supplier', 'txt', 'R', 'Is', 'gBal' , 'cp', 'cd', 'bal', 'gwa')

class stone_form(forms.ModelForm):
    class Meta:
        model = stone
        fields= ('name','supplier', 'quantity_Details', 'amount')


class jType_form(forms.ModelForm):
    class Meta:
        model = jType
        fields= ('id','jtype')
