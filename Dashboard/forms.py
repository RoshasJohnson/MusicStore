from pyexpat import model
from tkinter.tix import Form
from attr import field
from django import forms
from  customer.models import *


class Update_form(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
    
