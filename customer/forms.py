from .models import AbstractUser
from .models import Usercreation
from django import forms
from django.contrib.auth.forms import  UserCreationForm

class Customer(UserCreationForm):

    class Meta :
        model = Usercreation
        fields =['first_name','last_name','username','email','phone_number','password1','password2']

        
# CATEGORY_CHOICES =(
#     ("1", "String"),
#     ("2", "Keyborad"),
#     ("3", "Brass"),
#     ("4", "Woodwind"),
#     ("5", "Percussion"),
# )       

# class category(forms.Form):
#     category_type = forms.ChoiceField(choices = CATEGORY_CHOICES)
    