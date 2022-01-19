from dataclasses import fields
from pyexpat import model
from .models import AbstractUser, Design
from .models import Usercreation
from django import forms
from django.contrib.auth.forms import  UserCreationForm

class Customer(UserCreationForm):

    class Meta :
        model = Usercreation
        fields =['first_name','last_name','username','email','phone_number','password1','password2']

        
class sign(UserCreationForm):
    class Meta:
        model = Usercreation
        fields = ['username','password']








class DesignForm(forms.ModelForm):
    class Meta:
        model = Design
        fields = '__all__'              