from django import forms

class EmailForm(forms.Form):
    To = forms.EmailField(label='To', widget=forms.TextInput(attrs={
                                                                'class': 'form-control',
                                                                'autofocus': 'autofocus',
                                                            }))
    subject = forms.CharField(label='Subject',widget=forms.TextInput(attrs={
                                                                'class': 'form-control',
                                                                'autofocus': 'autofocus',
                                                            }))
    mass = forms.CharField(label='Massage',widget=forms.Textarea(attrs={
                                                                'class': 'form-control',
                                                                'autofocus': 'autofocus',
                                                                'style': 'padding-top: 2.375rem',
                                                            }))