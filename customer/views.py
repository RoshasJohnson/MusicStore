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
from sqlalchemy import false 
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
                request.session['name'] = 'username'
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
        return render(request,'customer/selected_product.html',{'selectedProduct':selectedProduct })


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
            return render(request,'customer/signin.html',{'errorshowing': errorshowing,'form':form})
    else:
        try:
            del request.session['name']
        except  KeyError as name:
            print('error')
        form = Customer()

        
        return render(request,'customer/signin.html',{'form':form })
    

    

#-----------------------------------------------------------------------------------  
# user sign in view


def register_USer_View(request):
    form = Customer()
    return render (request,'customer/register.html',{'form':form})



#-----------------------------------------------------------------------------------  

# def cart_View(request):
#     if request.session.get('name'):
#         return render(request,'customer/cart.html')
#     else:
#         error = 'you must login in  before add to cart'
#         form = Customer()
#         return render(request,'customer/signin.html',{'form':form ,'error':error})
# #-----------------------------------------------------------------------------------      


   
# def _cart_Id(request):
#     cart = request.session.session_key
#     if not cart:
#         cart = request.session.create()
#     return cart 


# def addto_cart_View(request):
#     # del request.session['cartdata']
#     cart = {}
#     cart[str(request.GET['id'])]= {
#         'title':request.GET['title'],
#         'qty':request.GET['qty'],
#         'price':request.GET['price'], 
#     }
#     print(cart,'??????????????????????????????????????????????????????????????????????????')        
#     if 'cartdata' in  request.session:
#         if str(request.GET['id']) in  request.session['cartdata'] :
#             cart_data = request.session['cartdata'] 
#             cart_data[str(request.GET['id'])]['qty'] = int(cart[str(request.GET['id'])]['qty'])
#             cart_data.update(cart_data)
#             request.session['cartdata'] = cart_data    
#         else:
#             cart_data = request.session['cartdata']    
#             cart_data.update(cart)
#             request.session['cartdata'] = cart_data
#     else:
#         request.session['cartdata'] = cart
#         print(cart)                          
#     return JsonResponse({'data': request.session['cartdata'],'totalitms':len(request.session['cartdata'])})



def cart_View(request): 
    if request.user.is_authenticated or request.session.get('name'): 
        user = request.user
        customer = request.user
        print(customer)
        order,create = Order.objects.get_or_create(Customer = customer,complete =  False)
        items  = order.orderitem_set.all()
    else:
        items = []
    # items = Order.objects.filter( Customer  = customer )
    # print(items,'llllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllll') 
    # contex = {'items':items} 
        # if request.user.is_authenticated :
            #     cart = {}
            #     cart[str(request.POST['id'])]= {
            #         'tittle':request.POST.get('title'),
            #         'qty':request.POST.get('qty'),
            #         'price':request.POST.get('price'), 
            #     }
            #     print(cart,'//////////////////////////////////////////////////////////////////////////////////////')
    contex = {'items':items}            
    return render (request,'customer/cart.html', contex)
        # else:
        #      print('working//////////////////////////////////////////////////////////')
        #      return render(request,'customer/signin.html')
# else:
#     return redirect('signin/')
 
 

def updateItem(request):
    data  = json.loads(request.body)
    productId  = data['productId']
    action = data['action']
    print('productId:',productId) 
    print('action:',action)
    user = request.user.UserCreation
    product =Product.objects.get(id= productId)
    return JsonResponse('item was added', safe = False) 