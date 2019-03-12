from django import forms
from .models import *

class EarringForm(forms.ModelForm):
    class Meta:
        model = Earrings
        fields = ('category', 'slug', 'date', 'description', 'charges', 'stones', 'weight', 'qty', 'craft_id', 'status', 'issues', 'image')

class NecklacesForm(forms.ModelForm):
    class Meta:
        model = Necklaces
        fields = ('category', 'slug', 'date', 'description', 'charges', 'stones', 'weight', 'qty', 'craft_id', 'status', 'issues', 'image')

class RingForm(forms.ModelForm):
    class Meta:
        model = Ring
        fields = ('category', 'slug', 'date', 'description', 'charges', 'stones', 'weight', 'qty', 'craft_id', 'status', 'issues', 'image')

class PendantForm(forms.ModelForm):
    class Meta:
        model = Pendants
        fields = ('category', 'slug', 'date', 'description', 'charges', 'stones', 'weight', 'qty', 'craft_id', 'status', 'issues', 'image')

