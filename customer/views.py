from itertools import product
from logging import exception
from os import name
from unicodedata import category
from django.http import HttpResponse
from django.shortcuts import redirect, render
import re 
import customer
from .models import AbstractUser, Product
from .models import *
from .forms import *
from django.contrib.auth import authenticate
from django import template
register = template.Library()


# Create your views here.

def category_view(request):
    contex = Category.objects.all()
    print(contex,'''''''''''''''''''''''''''''''''''''''''''''''')
    return render(request,'customer/header.html',{'context':contex})
#-----------------------------------------------------------------------------------      
@register.inclusion_tag('customer/header.html')    
def  category_view(poll):
      choices = poll.Category.objects.all()
      print(choices ,'''''''''''''''''''''''''''''''''''''''''''''''')
      return {'choices': choices}
#-----------------------------------------------------------------------------------  

# This function for registring the user
def usersignupView (request):
    if request.method == 'POST':
        form = Customer(request.POST)
        if form.is_valid():                 
                form.save()                
                # request.session['name'] = 'username'
                return render(request,'customer/otp.html') 
                

    else:
        form = Customer()
    return render(request,'customer/register.html',{'form':form})


#-----------------------------------------------------------------------------------      
# home page view function
def homepage_view(request):
    if request.session.get('name'):
        Designpage= Design.objects.all()[0]
        everyproduct = Product.objects.all()
        return render(request,'customer/index.html',{'everyproduct':everyproduct,'Designpage':Designpage})
    else:
        Designpage = Design.objects.all()
        everyproduct = Product.objects.all()
        return render(request,'customer/index.html',{'everyproduct':everyproduct,'Designpage':Designpage})


#-----------------------------------------------------------------------------------
# select Prdoucted view function
  

def selected_Product_view(request,id):
    if request.session.get('name'):
        selectedProduct = Product.objects.filter(id= id)

        return render(request,'customer/selected_product.html',{'selectedProduct':selectedProduct })
    else:
        selectedProduct = Product.objects.filter(id= id)
        return render(request,'customer/product-detail.html',{'selectedProduct':selectedProduct })


#-----------------------------------------------------------------------------------  
# sign in view funciton


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
# user sign in view


def register_USer_View(request):
    form = Customer()
    return render (request,'customer/register.html',{'form':form})



#-----------------------------------------------------------------------------------  

def cart_View(request):
    return render(request,'customer/cart.html')

#-----------------------------------------------------------------------------------      

def _cart_Id(request):
    cart = request.session.session_key
    if not cart:
        cart = request.session.create()
    return cart 

   


def addto_cart_View(request,id):
    product = Product.objects.get(id = id)
    try:
        cart  = Cart.objects.get(id = int(_cart_Id(request))) # get the cart using  cart id  present in the session
    
    except Cart.DoesNotExist:
        cart =  Cart.object.create(
            cart_id = _cart_Id(request)
        )
    cart.save()
    try:
        cart_item = CartItem.objects.get(product  = product,cart=cart)
        cart_item.quantity += 1
    except cart_item.DoesNotExist:
        cart_item = CartItem.objects.create(
            product  = product,
            quantity = 1,
            cart = cart

        ) 
        cart_item.save()               
    return redirect('cart')     