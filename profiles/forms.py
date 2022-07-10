from django import forms
from django.core import validators
from django.db.models import fields
from django.forms import widgets
from .models import User


class UserAdd(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'middle_name', 'last_name', 'address',
                  'contact_number', 'email', 'password']
        labels = {'first_name': 'First Name', 'middle_name': 'Middle Name', 'last_name': 'Last Name', 'address': 'Address',
                  'contact_number': 'Contact Number', 'email': 'Email', 'password': 'Password'}
        widgets = {'first_name': forms.TextInput(attrs={'class': 'form-control'}),
                   'middle_name': forms.TextInput(attrs={'class': 'form-control'}),
                   'last_name': forms.TextInput(attrs={'class': 'form-control'}),
                   'address': forms.TextInput(attrs={'class': 'form-control'}),
                   'contact_number': forms.TextInput(attrs={'class': 'form-control'}),
                   'email': forms.EmailInput(attrs={'class': 'form-control'}),
                   'password': forms.PasswordInput(render_value=True, attrs={'class': 'form-control'})
                   }
