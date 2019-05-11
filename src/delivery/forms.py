from django import forms
from .models import *


class DeliveryForm(forms.ModelForm):
    class Meta:
        model = DeliveryInfo
        fields = ('Order_No', 'UserName', 'Receiver_Name', 'Receiver_Add', 'District', 'Telephone_No', 'Deliver_date')

    def __init__(self, *args, **kwargs):
        super(DeliveryForm, self).__init__(*args, **kwargs)
        instance = getattr(self, 'instance', None)
        if instance and instance.id:
            self.fields['UserName'].widget.attrs['readonly'] = True
            self.fields['Order_No'].widget.attrs['readonly'] = True


class DeliveyDistanceForm(forms.ModelForm):
    class Meta:
        model = DeliveryDistance
        fields = ('Destination', 'Distance', 'Price')


class StaffDelivery(forms.ModelForm):
    class Meta:
        model = Delivery_Address
        fields = ('Receiver_Name', 'Receiver_Add', 'District', 'Delivery_Process')


#---------sangeeth----------
class DeliveryAddressForm(forms.ModelForm):
    class Meta:
        model = Delivery_Address
        fields = [
        #     'billing_profile',
        #     'address_type',
                'Receiver_Name',
                'Receiver_Add',
                'District',
        ]


