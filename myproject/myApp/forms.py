from django import forms
from .models import *

class RegisterForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter your name'}))
    email = forms.EmailField(widget=forms.TextInput(attrs={'placeholder': 'Enter your email'}))
    Phonenumber = forms.CharField(label='Mobile Number',widget=forms.TextInput(attrs={'placeholder': 'Enter your phone number'}))
    address = forms.CharField(widget=forms.Textarea)
    class Meta:
        model=RegisterModel
        fields = ['name', 'email', 'Phonenumber', 'address']
        