from django import forms
from .models import *

class TransForm(forms.ModelForm):
    class Meta:
        model = BankDetails
        fields = ('Trans_ID', 'Trans_Date','Bank_Name', 'Bank_Branch', 'Amount', 'Withdraw_or_Deposit', 'Trans_Type', 'Transfer_Details')


