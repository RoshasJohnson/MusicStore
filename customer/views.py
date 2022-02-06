from audioop import add
from cgi import print_environ
from copy import error
from itertools import product
import json
from logging import exception
from multiprocessing import context
from os import name
from ssl import HAS_TLSv1_1
from unicodedata import category
from urllib import request
from urllib.request import Request
from venv import create
from xmlrpc.client import DateTime
from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect, render
import re
from django.views.decorators.csrf import csrf_protect
import datetime
 
from pyparsing import replaceWith
from sqlalchemy import false, null 
import customer
from .models import AbstractUser, Product
from .models import *
from .forms import *
from django.contrib.auth import authenticate
from django import template
import os
from twilio.rest import Client
from twilio.rest import TwilioRestClient
num = ''


# Create your views here.



register = template.Library()
@register.inclusion_tag('customer/header.html')

def inclusiontag(request):
    choices =Category.objects.all()
    contex = {'choices': choices}
    return render(request, "customer/header.html",  contex )
#-----------------------------------------------------------------------------------  
def send_otp(number):
    global num 
    num = number
    print(num)
   
    account_sid = os.environ['TWILIO_ACCOUNT_SID'] = "ACd4a2de1fd0a5c88226ee5ac56a0a7537"
    print('hi')
    auth_token = os.environ['TWILIO_AUTH_TOKEN'] = "d727068391b561c96969eaf9e13ee3b0"
    print('hello')
    client = Client(account_sid, auth_token)
    print('hello world')
    verification = client.verify \
                                .services('MG3f5e19a03bfe66999d0cc3e3ade29c23') \
                                .verifications \
                                .create(to=num, channel='sms')
    print('is it ?')                            
    print(verification.status)
  

    
 
def Otp_Verification(otp):
    global num
    
    account_sid = os.environ['TWILIO_ACCOUNT_SID'] = "AC36f1ef84ddb97566b6ffa82bdaa66a92"
    auth_token = os.environ['TWILIO_AUTH_TOKEN'] = "07764f0972ae242906357de25f058630"
    client = Client(account_sid, auth_token)

    verification_check = client.verify \
                            .services('VA4291d9583481a66d33b553ff12d639c1') \
                            .verification_checks \
                            .create(to=num, code=otp)
    print(verification_check.status)
    print(verification_check)

    if verification_check.status ==  'approved':
        return True
    else:
        return False










# This function for registring the user 
def usersignupView (request):
    if request.method == 'POST':
        form = Customer(request.POST)
        if form.is_valid():                 
                request.session['name'] = request.POST['username']
                num = request.POST['phone_number']
                print(num)
                number = '+91'+num
                print(number)
                send_otp(number)
                # form.save()                 
                return render(request,'customer/otp.html')                  
    else:
        form = Customer()
    choices =Category.objects.all()
    contex = {'form':form,'choices': choices}    
    return render(request,'customer/register.html',contex)

 
#-----------------------------------------------------------------------------------      
# home page view function
def homepage_view(request):
    Designpage= Design.objects.all()    
    print(len(Designpage))     
    if request.session.get('name'):
        user = request.session.get('name')
        print(user)
        customer = request.session.get('name')
        user     = Usercreation.objects.get(username = customer)
        everyproduct = Product.objects.all()
        choices =Category.objects.all() 
        cartcount=  OrderItem.objects.filter(user = user  ).count()
        cartitems = OrderItem.objects.filter(user = user).all
      
        contex = {'everyproduct':everyproduct,
        'Designpage':Designpage,
        'choices':choices,
        'cartcount':cartcount,'cartitems':cartitems}
        return render(request,'customer/index.html',contex)

    else:
         
        Designpage = Design.objects.all()
        everyproduct = Product.objects.all()
        choices =Category.objects.all()
        order=  OrderItem.objects.all().count()
        contex = {'everyproduct':everyproduct,
        'Designpage':Designpage,
        'choices':choices,
        'order':order,'shipping ':False}
        return render(request,'customer/index.html',contex)


#------------------------ -----------------------------------------------------------
# select Prdoucted view function
  
  
def selected_Product_view(request,id):
    if request.session.get('name'):
        selectedProduct = Product.objects.filter(id= id) 
        choices =Category.objects.all()
        customer = request.session.get('name')
        user     = Usercreation.objects.get(username = customer)
        cartcount=  OrderItem.objects.filter(user = user  ).count()
        contex = {'selectedProduct':selectedProduct,'choices':choices,'cartcount':cartcount }
        return render(request,'customer/selected_product.html',contex)
    else:
        selectedProduct = Product.objects.filter(id= id) 
        choices =Category.objects.all()
        # cartcount=  OrderItem.objects.all().count()
        contex = {'selectedProduct':selectedProduct,'choices':choices,'shipping ':False}
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
             request.session['name'] = request.POST['username']
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
    if  request.session.get('name'): 
        user = request.session.get('name')
        customer = Usercreation.objects.get(username = user)
        cartcount=  OrderItem.objects.filter(user = customer).count()
        print(customer)
        items  = OrderItem.objects.filter( user = customer)
        sum  = 0
        for i in items:
            sum += i.quantity  * i.product.product_prize 
      
    else:   
        items = [] 
        error = "you have'nt carts"
        return render(request,'customer/cart.html',{'error':error, 'choices':choices})
    contex = {'items':items, 'choices':choices,'cartcount': cartcount,'sum':sum}
    return render (request,'customer/cart.html', contex)

 
 



def checkout_view(request):         
    choices =Category.objects.all()
    if  request.session.get('name'): 
        customer = request.session.get('name')
        print(customer)
        user = Usercreation.objects.get(username= customer)
        Items  = OrderItem.objects.filter(user = user)
        form = CustomerAdress.objects.filter(user = user)
        cartcount=  OrderItem.objects.filter(user = user  ).count()
        print(Items)
        sum = 0

        for i in Items:
                sum += i.quantity  * i.product.product_prize
        print(sum)
        tax = int(sum/18)
        grandtotal = tax+sum+40
        print(tax)
        print(grandtotal)


        
    else:
        return redirect('cart/')
    contex = {'Items':Items,'choices':choices,'form':form,'tax':tax,'grandtotal':grandtotal,'cartcount': cartcount}  
    return render(request,'customer/checkout.html',contex)




 
 

@csrf_protect
def updateItem(request):
    if request.session.get('name'): 
        data  = json.loads(request.body)    
        productId  = data['productId']
        action = data['action']
        
        print(action,'_-------------________________--------------------------------')
        customer = request.session.get('name')
        print(customer,'fffffffffffffffffffffffffffffffffffff')
        user = Usercreation.objects.get(username = customer)
        product = Product.objects.get(id = productId  ) 
        OrderItem.objects.create(product = product ,user = user )
        return JsonResponse('item was added', safe = False)    



@csrf_protect
def place_orderView(request):
    customer = request.user
    data  = json.loads(request.body) 
    action = data['action']
    print(data)
    print(action)
    if action == 'cod':
            print('This is cash on delevery')
            
            user = OrderItem.objects.get_or_create(Customer = customer,complete =  False)
            delverycod =  OrderItem.objects.all()
            # return render (request,'customer/index.html')
            print(delverycod)
            print(user)
            for i in OrderItem:
                pass

            # delverycod = Order.objects.create(complete =  False)
            # delverycod.append(Order) 
            # order.delete()  
       

    return JsonResponse('success', safe = False)  


def Process_orderView(request):
    data  = json.loads(request.body)
    action = data['action']
    print(action,'ffffffffffffffffffd' )
    return JsonResponse('ddddd', safe = False) 
       

def OrderView(request,id):
    choices =Category.objects.all()
    if request.session.get('name'):
        user = request.session.get('name')   
        Items = Product.objects.filter(id = id)
        user1  = Usercreation.objects.get(username = user)
        print(user1,'userrrrrrrrrrrrrrrrrrrrrrrrrrrrr')
        form = CustomerAdress.objects.filter(user = user1)
        cartcount=  OrderItem.objects.filter(user = user1).count()
        
        for i in Items:
            tax =int(( i.product_prize)/18)
            grandtotal  = tax+i.product_prize +40 
           
        context = {'Items':Items,'form':form,'tax':tax,
        'grandtotal':grandtotal,'choices':choices,'cartcount':cartcount} 
        print(grandtotal)
        return render(request,'customer/checkout-2.html',context) 
   

  
 
def addcartQtyView(request):
    if request.session.get('name'):
        data  = json.loads(request.body)
        action = data['action']
        productid = data['productId']
        orderItem = OrderItem.objects.get(id  = productid)
        if action == 'add':

            orderItem.quantity =(orderItem.quantity  + 1)
        elif action == 'remove':
            orderItem.quantity =(orderItem.quantity  - 1)
            orderItem.delete()
        if productid in data:    
            orderItem = OrderItem.objects.get(id = productid)
        orderItem.save()
        if orderItem.quantity <= 0:
           orderItem.delete()
        return JsonResponse('success', safe = False) 
   


def checkingaddressview(request):
    if request.session.get('name'):
    #     user1 = request.session.get('name')
    #     user   = Usercreation.objects.get( username = user1) 
    #     print(user,'/////////////////////////////////////////////////////')
    #     first_name   =  request.POST['first_name']
    #     last_name    = 	request.POST['last_name']
    #     email    	 =  request.POST['email']
    #     phone_number =	request.POST['phone_number']
    #     house_name   = 	request.POST['house_name']
    #     street_name  =	request.POST['street_name'] 
    #     city         =  request.POST['city']
    #     state	     =  request.POST['state']
    #     country	     =  request.POST['country']
    #     post_code    =  request.POST['post_code']
    #     print(email)  
    #     # address =CustomerAdress(request.POST or None)
    #     CustomerAdress.objects.create(user = user ,first_name = first_name,last_name = last_name,
    #     email = email,phone_number = phone_number,house_name = house_name
    #    ,street_name  = street_name,city = city,state = state,country = country,
    #     post_code = post_code )
    #     form = CustomerAdress.objects.filter(user = user) 
    #     # print(form,'pppppppppppppppppppppppppppppppppppppppp')
    #     # Buyorder = Product.objects.filter(id = id)
    #     # print(Buyorder,'jjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjj')
    #     # context = {'Buyorder':Buyorder}
        return render(request,'customer/checkout-2.html') 



def productpage_View(request,id):
    if request.session.get('name'):
        user = request.session.get('name')
        username = Usercreation.objects.get(username = user)
        cartcount=  OrderItem.objects.filter(user = username).count()       
        product = Category.objects.get(id = id)
        products   = Product.objects.filter(category_type = product)
        choices =Category.objects.all()
        print(products)
        context = {'products':products,'choices':choices,'cartcount':cartcount}
        return render (request,'customer/products.html',context) 
       
    else:      
        product = Category.objects.get(id = id)
        products   = Product.objects.filter(category_type = product)
        choices =Category.objects.all()
        print(products)
        context = {'products':products,'choices':choices}
        return render (request,'customer/products.html',context) 





@csrf_protect
def order_placingView(request):
    
    if request.session.get('name'):
         data  = json.loads(request.body)
         payment_method = data['payment']
         address_id = data['address']
         product_Id = data['productId'] 
         get_total  = data['get_total'] 
         print(type(get_total))

         print(get_total,'prize')
         user       = request.session.get('name')
         username   = Usercreation.objects.get(username= user)
         product    = Product.objects.get(id = product_Id)
         address    = CustomerAdress.objects.get(id = address_id ) 
         print(address,'address')
         print(payment_method,address,'hheeheheheheheheehhe')

         
         Order.objects.create( Customer = address,order_product =product,
         user_name = username,payment_method = payment_method ,total_prize =get_total)
         return JsonResponse('cash on delery', safe = False) 
   
        

def user_account_View(request):
    form = Customer()
    choices =Category.objects.all()
    if request.session.get('name'):
        user        =  request.session.get('name')
        username    =  Usercreation.objects.get(username  = user)
        order_all   =  Order.objects.filter(user_name = username).count()
        orders      =  Order.objects.filter(user_name = username)
        cartcount=  OrderItem.objects.filter(user = username).count()
    
    else:   
        error = "You must log in  for see your account" 
        context = {'form':form,'error':error}
        return render(request,'customer/signin.html',context)
    contex = {'order_all':order_all,'orders':orders,'cartcount':cartcount,'choices':choices,'user': user} 
    return render(request,'customer/user_account.html' ,contex)

     
def cart_item_buy_View(request):
     if request.session.get('name'):
         data  = json.loads(request.body)
         payment_method = data['payment']
         address_id = data['address']
         product_Id = data['productId'] 
         get_total  = data['get_total']
         user       = request.session.get('name') 
         print(type(get_total))
         print(product_Id,address_id)
         username = Usercreation.objects.get(username= user)
         product   = OrderItem.objects.filter(user = username)
         address   = CustomerAdress.objects.get(id = address_id  )
         
         print(address,'address')
         tax = 0
         for i in product:
             tax =i.product.product_prize/18   
             get_total =(i.product.product_prize+tax +40) *i.quantity 
             quantity =i.quantity 
             print(get_total,"quantity")
             Order( Customer = address, order_product  =i.product,
             user_name = username,payment_method = payment_method, quantity  =i.quantity ,total_prize =get_total).save()
             product.delete()
         return JsonResponse('cash-on-delevery for cart items' ,safe=False)





def add_new_address_View(request):
    form  = CustomerAdressForm()
    if request.method == 'POST':
        user1 = request.session.get('name')
        user   = Usercreation.objects.get( username = user1) 
        print(user,'/////////////////////////////////////////////////////')
        first_name   =  request.POST['first_name']
        last_name    = 	request.POST['last_name']
        phone_number =	request.POST['phone_number']
        house_name   = 	request.POST['house_name']
        street_name  =	request.POST['street_name'] 
        city         =  request.POST['city']
        state	     =  request.POST['state']
        country	     =  request.POST['country']
        post_code    =  request.POST['post_code']
        print(email)  
        CustomerAdress.objects.create(user = user ,first_name = first_name,last_name = last_name
        ,phone_number = phone_number,house_name = house_name
        ,street_name  = street_name,city = city,state = state,country = country,
            post_code = post_code )
        print('success')
        Items  = OrderItem.objects.filter(user = user)
        form = CustomerAdress.objects.filter(user = user)
        context = {'Items':Items,'form':form}  
        return render (request,'customer/checkout.html', context)  

    if request.session.get('name'):
        context  = {'form':form}
        return render (request,'customer/Add_address.html',context)


def add_new_addresforEachOrder_View(request,id):
    form  = CustomerAdressForm() 
    if request.session.get('name'):
        product_id = Product.objects.filter(id = id)
        for i  in product_id:
            print(i.id,'blah')
        print(len(product_id))
        context = {'form':form,'product_id':product_id} 
        return render (request,'customer/Add_address-2.html',context)




def newaddress_save_view(request,id):
     choices = Category.objects.all()
     if request.method == 'POST':
        user1 = request.session.get('name')
        user   = Usercreation.objects.get( username = user1) 
        print(user,'/////////////////////////////////////////////////////')
        first_name   =  request.POST['first_name']
        last_name    = 	request.POST['last_name']
        phone_number =	request.POST['phone_number']
        house_name   = 	request.POST['house_name']
        street_name  =	request.POST['street_name'] 
        city         =  request.POST['city']
        state	     =  request.POST['state']
        country	     =  request.POST['country']
        post_code    =  request.POST['post_code']
        print(email)  
        CustomerAdress.objects.create(user = user ,first_name = first_name,last_name = last_name
        ,phone_number = phone_number,house_name = house_name
        ,street_name  = street_name,city = city,state = state,country = country,
            post_code = post_code )
        print('success')
        cartcount  = OrderItem.objects.filter(user = user).count()
        Items  = Product.objects.filter(id = id)
        form = CustomerAdress.objects.filter(user = user)
        for i in Items:
            tax =int(( i.product_prize)/18)
            grandtotal  = tax+i.product_prize +40 
        context = {'Items':Items,'form':form,'tax':tax,
        'grandtotal':grandtotal,'choices':choices,'cartcount':cartcount} 
        return render (request,'customer/checkout-2.html', context)  