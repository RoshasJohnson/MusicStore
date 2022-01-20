from itertools import product
from os import name
from unicodedata import category
from django.shortcuts import render
import re 
import customer
from .models import AbstractUser, Product
from .models import *
from .forms import *
from django.contrib.auth import authenticate


# Create your views here.



# This function for registring the user
def usersignupView (request):
    if request.method == 'POST':
        form = Customer(request.POST)
        if form.is_valid():
            # Phone_Number = form.phone_number
            # r=re.fullmatch('[6-9][0-9]{9}',Phone_Number)
            # if r!=None:                 
                form.save()                
                request.session['name'] = 'username'
                return render(request,'customer/otp.html') 
            # else:
            #     error = 'Enter Valid phone number'
            #     return render('customer/register.html',{'eroor':error})            

    else:
        form = Customer()
    return render(request,'customer/register.html',{'form':form})


#----------------------------------------------------------------------------------- 
#     
#     

def homepage_view(request):
    if request.session.get('name'):
        Designpage= Design.objects.all()[0]
        print(Designpage.Banner_image1.url,'===================================================roshas')
        everyproduct = Product.objects.all()
        return render(request,'customer/index.html',{'everyproduct':everyproduct,'Designpage':Designpage})
    else:
        Designpage = Design.objects.all()
        print(Designpage,'===================================================')
        print('======================================================')
        everyproduct = Product.objects.all()
        return render(request,'customer/index.html',{'everyproduct':everyproduct,'Designpage':Designpage})


#-----------------------------------------------------------------------------------
# 
  

def selected_Product_view(request,id):
    if request.session.get('name'):
        selectedProduct = Product.objects.filter(id= id)
        return render(request,'customer/selected_product.html',{'selectedProduct':selectedProduct })
    else:
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

