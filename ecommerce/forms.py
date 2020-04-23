from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Contact


# class signUpForm(UserCreationForm):
#     last_name = forms.CharField(max_length=100, help_text='Last Name')
#     first_name = forms.CharField(max_length=100, help_text='First Name')
#     email = forms.EmailField(max_length=150, help_text='Email')
#
#     class Meta:
#         model = Profile
#         fields = ['username', 'first_name', 'last_name', 'email', 'password', 'password1']

# class ContactForm(forms.ModelForm):
#     class Meta: 
#         model = Contact
#         fields = ('first_name','last_name','email','message')