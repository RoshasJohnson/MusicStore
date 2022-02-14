from dataclasses import fields


from pyparsing import Or
from .models import AbstractUser, CustomerAdress, Design, Order
from .models import Usercreation
from django import forms
from django.contrib.auth.forms import  UserCreationForm

class Customer(UserCreationForm):

    class Meta :
        model = Usercreation
        fields =['first_name','last_name','username','email','phone_number','password1','password2']



class Edit_Profile(UserCreationForm):
    class Meta:
         model = Usercreation
         fields =['first_name','last_name','username','email','phone_number']
      



class DesignForm(forms.ModelForm):
    class Meta:
        model = Design
        fields = '__all__'


class CustomerAdressForm(forms.ModelForm):
    class Meta :
        model = CustomerAdress 
        fields = ['first_name','last_name','email','phone_number','house_name','street_name','city'
        ,'state','country','post_code']  


        
class OrderForm(forms.ModelForm):
    class Meta :
        model = Order 
        fields = ['status']

            