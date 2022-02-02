from dataclasses import fields
from pyexpat import model
from .models import AbstractUser, CustomerAdress, Design
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


class CustomerAdressForm(forms.ModelForm):
    class Meta :
        model = CustomerAdress 
        fields = ['first_name','last_name','email','phone_number','house_name','street_name','city'
        ,'state','country','post_code']  
      