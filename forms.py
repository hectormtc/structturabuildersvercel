# apps/accounts/forms.py
from django import forms
from django.contrib.auth.forms import AuthenticationForm
from .models import Customer

class LoginForm(AuthenticationForm):
    pass

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['name', 'email', 'phone']