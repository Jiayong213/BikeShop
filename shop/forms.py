from django import forms

class BikeOrderForm(forms.Form):
    name = forms.CharField(label='your name: ', max_length=100)
    surname = forms.CharField(label='your surname: ', max_length=100)
    phone_number = forms.CharField(label='your phone number: ', max_length=100)