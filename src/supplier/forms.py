
from django import forms
from .models import *

class add_supplierForm(forms.ModelForm):
    class Meta:
        model = supplier
        fields = ('first_Name', 'last_Name', 'nic', 'address', 'phone_No','supplier_item')

class edit_Supplier(forms.ModelForm):
    class Meta:
        model = supplier
        fields = ('first_Name', 'last_Name', 'nic', 'address', 'phone_No', 'supplier_item')