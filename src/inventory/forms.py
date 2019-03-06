from django import forms
from .models import *

class EarringForm(forms.ModelForm):
    class Meta:
        model = Earrings
        fields = ('cat', 'date', 'description', 'charges', 'stones', 'weight', 'qty', 'craft_id', 'status', 'issues', 'image')

class NecklacesForm(forms.ModelForm):
    class Meta:
        model = Necklaces
        fields = ('cat', 'date', 'description', 'charges', 'stones', 'weight', 'qty', 'craft_id', 'status', 'issues', 'image')

class RingForm(forms.ModelForm):
    class Meta:
        model = Ring
        fields = ('cat', 'date', 'description', 'charges', 'stones', 'weight', 'qty', 'craft_id', 'status', 'issues', 'image')

class PendantForm(forms.ModelForm):
    class Meta:
        model = Pendants
        fields = ('cat', 'date', 'description', 'charges', 'stones', 'weight', 'qty', 'craft_id', 'status', 'issues', 'image')

