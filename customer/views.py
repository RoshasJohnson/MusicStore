from django.shortcuts import render
from .models import AbstractUser
from .forms import *
from django.contrib.auth import authenticate


# Create your views here.



# This function for registring the user
def user_signup(request):
    if request.method == 'POST':
        form = Customer(request.POST)
        if form.is_valid():
            form.save()
            #   if  form is not None :
            # request.session['pk'] = username
            return render(request,'customer/otp.html') 

    # elif  request.session.has_key('pk') :
    #     return render(request,'customer/otp.html') 
    else:
        form = Customer()
    return render(request,'customer/register.html',{'form':form})
    