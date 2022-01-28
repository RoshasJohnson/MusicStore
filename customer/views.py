from cgi import print_environ
from copy import error
from itertools import product
import json
from logging import exception
from os import name
from unicodedata import category
from venv import create
from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect, render
import re

from pyparsing import replaceWith
from sqlalchemy import false, null 
import customer
from .models import AbstractUser, Product
from .models import *
from .forms import *
from django.contrib.auth import authenticate
from django import template
register = template.Library()
@register.inclusion_tag('customer/header.html')


# Create your views here.

# def category_view(request):
#     contex = Category.objects.all()
#     print(contex,'''''''''''''''''''''''''''''''''''''''''''''''')
#     return render(request,'customer/header.html',{'context':convtex})
#----------------------------------------------------v\-------------------------------      
  
def inclusiontag(request):
    choices =Category.objects.all()
    contex = {'choices': choices}
    return render(request, "customer/header.html",  contex )
#-----------------------------------------------------------------------------------  
 
# This function for registring the user 
def usersignupView (request):
    if request.method == 'POST':
        form = Customer(request.POST)
        if form.is_valid():                 
                form.save()                 
                request.session['name'] = 'username'
                return render(request,'customer/otp.html') 
                
 
    else:
        form = Customer()
    choices =Category.objects.all()
    contex = {'form':form,'choices': choices}    
    return render(request,'customer/register.html',contex)


#-----------------------------------------------------------------------------------      
# home page view function
def homepage_view(request):
    if request.session.get('name'):
        Designpage= Design.objects.all()[0]
        everyproduct = Product.objects.all()
        choices =Category.objects.all() 
        cartItems = Order.get_cart_items
        contex = {'everyproduct':everyproduct,
        'Designpage':Designpage,
        'choices':choices,
        'cartItems':cartItems}
        return render(request,'customer/index.html',contex)


    else:
        Designpage = Design.objects.all()
        everyproduct = Product.objects.all()
        choices =Category.objects.all()
        cartItems = Order.get_cart_items
        contex = {'everyproduct':everyproduct,
        'Designpage':Designpage,
        'choices':choices,
        'cartItems':cartItems}
        return render(request,'customer/index.html',contex)


#-----------------------------------------------------------------------------------
# select Prdoucted view function
  

def selected_Product_view(request,id):
    selectedProduct = Product.objects.filter(id= id) 
    choices =Category.objects.all()
    cartItems = Order.get_cart_items
    contex = {'selectedProduct':selectedProduct,'choices':choices,'cartItems':cartItems }
    return render(request,'customer/selected_product.html',contex)
    


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
             request.session['name'] = 'username'
             return redirect('/')
        else:
            errorshowing = 'Incorrect user name and password'
            choices =Category.objects.all()
            return render(request,'customer/signin.html',{'errorshowing': errorshowing,'form':form, 'choices':choices})
    else:
        try:
            del request.session['name']
        except  KeyError as name:
            print('error')
        form = Customer()
        choices =Category.objects.all()
        
        return render(request,'customer/signin.html',{'form':form, 'choices':choices })
    

    

#-----------------------------------------------------------------------------------  
# user sign in view


def register_USer_View(request):
    choices =Category.objects.all()
    form = Customer()
    return render (request,'customer/register.html',{'form':form, 'choices':choices})



#-----------------------------------------------------------------------------------  

def cart_View(request): 
    choices =Category.objects.all()
    if request.user.is_authenticated or request.session.get('name'): 
        user = request.user
        customer = request.user
        print(customer)
        order,create = Order.objects.update_or_create(Customer = customer,complete =  False)
        items  = order.orderitem_set.all()
       
    else:
        items = [] 
        error = "you have'nt carts"
        return render(request,'customer/cart.html',{'error':error, 'choices':choices})
    contex = {'items':items,'order':order, 'choices':choices}
    return render (request,'customer/cart.html', contex)

 
 




def checkout_view(request):
    choices =Category.objects.all()
    if request.user.is_authenticated or  request.session.get('name'): 
        user = request.user
        customer = request.user
        print(customer)
        order,create = Order.objects.get_or_create(Customer = customer,complete =  False)
        items  = order.orderitem_set.all()
       
    else:
        return redirect('cart/')
 
    contex = {'items':items,'order':order, 'choices':choices}  
    return render(request,'customer/checkout.html',contex)




 


def updateItem(request): 
    data  = json.loads(request.body)    
    productId  = data['productId']
    action = data['action']
    print(productId,'_-------------________________--------------------------------')
    customer = request.user
    product = Product.objects.get(id = productId  )
    order,create = Order.objects.get_or_create(Customer = customer,complete =  False)
    orderItem,create = OrderItem.objects.get_or_create(order = order,product = product)

    if action == 'add':
        orderItem.quantity =(orderItem.quantity  + 1)
    elif action == 'remove':
        orderItem.quantity =(orderItem.quantity  - 1)
    
    orderItem.save()

    if orderItem.quantity <= 0:
        orderItem.delete()
    return JsonResponse('item was added', safe = False)   