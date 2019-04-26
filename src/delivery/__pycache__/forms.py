from django import forms
from .models import *

class DeliveryForm(forms.ModelForm):
    class Meta:
        model = DeliveryInfo
        fields = ('Order_No', 'UserName', 'Receiver_Name', 'Receiver_Add', 'Telephone_No', 'Deliver_date')

class StaffDelivery(forms.ModelForm):
    class Meta:
        model = DeliveryInfo
        fields = ('Order_No', 'UserName', 'Receiver_Name', 'Receiver_Add', 'Telephone_No', 'Deliver_date', 'Delivery_Process')


