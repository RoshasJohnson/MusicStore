from itertools import product
from django.shortcuts import render

import customer
from .models import AbstractUser, Product
from .forms import *
from django.contrib.auth import authenticate


# Create your views here.



# This function for registring the user
def usersignupView  (request):
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


#----------------------------------------------------------------------------------- 
# 
#    

def homepage_view(request):
    everyproduct = Product.objects.all()
    
    return render(request,'customer/index.html',{'everyproduct':everyproduct})


#-----------------------------------------------------------------------------------
# 
  

def selected_Product_view(request,id):
    selectedProduct = Product.objects.filter(id= id)
    return render(request,'customer/selected_product.html',{'selectedProduct':selectedProduct })





#-----------------------------------------------------------------------------------  
def signIcon_view(request):
    form = Customer()
    form = Customer(request.POST or None,request.FILES or None)
    if request.method == 'POST':
        userlogin = authenticate(username = request.POST['username'],password = request.POST['password1'])
        username  = request.POST['username']
        
        if userlogin is not None:
             usercheck = Usercreation.objects.get(username = username)
             return render (request,'customer/Home.html')
        else:
            errorshowing = 'Incorrect user name and password'
            return render(request,'customer/signin.html',{'errorshowing': errorshowing,'form':form})
    else:
        form = Customer()
        return render(request,'customer/signin.html',{'form':form })




#-----------------------------------------------------------------------------------  

def register_USer_View(request):
    form = Customer()
    return render (request,'customer/register.html',{'form':form}   )



#-----------------------------------------------------------------------------------  

