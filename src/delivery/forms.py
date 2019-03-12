from django import forms
from .models import *

class DeliveryForm(forms.ModelForm):
    class Meta:
        model = DeliveryInfo
        fields = ('Order_No', 'UserName', 'Receiver_Name', 'Receiver_Add', 'Telephone_No', 'Deliver_date')