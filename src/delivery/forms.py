from django import forms
from .models import *

class DeliveryForm(forms.ModelForm):
    class Meta:
        model = DeliveryInfo
        fields = ('Order_No','Item_Code','Description','Weight','Receiver_Name','Receiver_Add','Deliver_date')