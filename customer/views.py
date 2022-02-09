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
from datetime import datetime, timedelta
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
                num          = request.POST['phone_number']
                print(num)
                number       = '+91'+num
                print(number)
                # send_otp(number)
                form.save()                 
                return render(request,'customer/otp.html')                  
    else:
        form = Customer()
    choices  = Category.objects.all()
    contex   = {'form':form,'choices': choices}    
    return render(request,'customer/register.html',contex)

 
#-----------------------------------------------------------------------------------      
# home page view function
def homepage_view(request):
    Designpage= Design.objects.all()    
    print(len(Designpage))     
    if request.session.get('name'):
        user        = request.session.get('name')
        customer     = request.session.get('name')
        user         = Usercreation.objects.get(username = customer)
        everyproduct = Product.objects.all()
        choices      = Category.objects.all() 
        cartcount    =  OrderItem.objects.filter(user = user  ).count()
        cartitems    = OrderItem.objects.filter(user = user).all
      
        contex = {'everyproduct':everyproduct,
        'Designpage':Designpage,
        'choices':choices,
        'cartcount':cartcount,'cartitems':cartitems,'user':user}
        return render(request,'customer/index.html',contex)

    else:
        user = request.session.get('name') 
        Designpage   = Design.objects.all()
        everyproduct = Product.objects.all()
        choices      = Category.objects.all()
        order        =  OrderItem.objects.all().count()
        contex       = {'everyproduct':everyproduct,
        'Designpage':Designpage,
        'choices':choices,
        'order':order,'user':user}
        return render(request,'customer/index.html',contex)


#------------------------ -----------------------------------------------------------
# select Prdoucted view function
  
  
def selected_Product_view(request,id):
    if request.session.get('name'):
        selectedProduct = Product.objects.filter(id= id) 
        choices         = Category.objects.all()
        customer        = request.session.get('name')
        user            = Usercreation.objects.get(username = customer)
        cartcount       =  OrderItem.objects.filter(user = user  ).count()
        contex          = {'selectedProduct':selectedProduct,'choices':choices,'cartcount':cartcount }
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
        userlogin       = authenticate(username = request.POST['username'],password = request.POST['password1'])
        username        = request.POST['username']
        
        if userlogin is not None:
             usercheck  = Usercreation.objects.get(username = username)
             request.session['name'] = request.POST['username']
             return redirect('/')
        else:
            errorshowing = 'Incorrect user name and password'
            choices      =   Category.objects.all()
            return render(request,'customer/signin.html',{'errorshowing': errorshowing,'form':form, 'choices':choices})
    else: 
        try:
            del request.session['name']
        except  KeyError as name:
            print('error')
        form    = Customer()
        choices = Category.objects.all()
        
        return render(request,'customer/signin.html',{'form':form, 'choices':choices })
    

    

#-----------------------------------------------------------------------------------  
# user sign in view


def register_USer_View(request):
    choices =   Category.objects.all()
    form    = Customer()
    return render (request,'customer/register.html',{'form':form, 'choices':choices})


 
#-----------------------------------------------------------------------------------  

def cart_View(request): 

    choices        =   Category.objects.all()
    if  request.session.get('name'): 
        user       = request.session.get('name')
        customer   = Usercreation.objects.get(username = user)
        cartcount  =  OrderItem.objects.filter(user = customer).count()
        items      = OrderItem.objects.filter( user = customer)
        sum        = 0
        for i in items:
            sum += i.quantity  * i.product.product_prize 
      
    else:   
        items = [] 
        error = "you have'nt carts"
        return render(request,'customer/cart.html',{'error':error, 'choices':choices})
    contex = {'items':items, 'choices':choices,'cartcount': cartcount,'sum':sum}
    return render (request,'customer/cart.html', contex)

 
 



def checkout_view(request):         
    choices       =   Category.objects.all()
    if  request.session.get('name'): 
        customer  = request.session.get('name')
        user      = Usercreation.objects.get(username= customer)
        Items     = OrderItem.objects.filter(user = user)
        form      = CustomerAdress.objects.filter(user = user)
        cartcount =  OrderItem.objects.filter(user = user  ).count()
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
        data       = json.loads(request.body)    
        productId  = data['productId']
        action     = data['action']
        
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
    data     = json.loads(request.body) 
    action   = data['action']
    if action == 'cod':
            print('This is cash on delevery')
            
            user       = OrderItem.objects.get_or_create(Customer = customer,complete =  False)
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
    data   = json.loads(request.body)
    action = data['action']
    return JsonResponse('ddddd', safe = False) 
       

def OrderView(request,id):
    choices       = Category.objects.all()
    if request.session.get('name'):
        user      = request.session.get('name')   
        Items     = Product.objects.filter(id = id)
        user1     = Usercreation.objects.get(username = user)
        form      = CustomerAdress.objects.filter(user = user1)
        cartcount = OrderItem.objects.filter(user = user1).count()
        
        for i in Items:
            tax =int(( i.product_prize)/18)
            grandtotal  = tax+i.product_prize +40 
           
        context = {'Items':Items,'form':form,'tax':tax,
        'grandtotal':grandtotal,'choices':choices,'cartcount':cartcount} 
        print(grandtotal)
        return render(request,'customer/checkout-2.html',context) 
   

  
 
def addcartQtyView(request):
    if request.session.get('name'):
        data      = json.loads(request.body)
        action    = data['action']
        productid = data['productId']
        orderItem = OrderItem.objects.get(id  = productid)
        if action == 'add':
            orderItem.quantity =(orderItem.quantity  + 1)
        elif action  == 'remove':
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
        user      = request.session.get('name')
        username  = Usercreation.objects.get(username = user)
        cartcount =  OrderItem.objects.filter(user = username).count()       
        product   = Category.objects.get(id = id)
        products  = Product.objects.filter(category_type = product)
        choices   = Category.objects.all()
        context   = {'products':products,'choices':choices,'cartcount':cartcount}
        return render (request,'customer/products.html',context) 
       
    else:      
        product    = Category.objects.get(id = id)
        products   = Product.objects.filter(category_type = product)
        choices    = Category.objects.all()
        context    = {'products':products,'choices':choices}
        return render (request,'customer/products.html',context) 





@csrf_protect
def order_placingView(request):
    
    if request.session.get('name'):
         data           = json.loads(request.body)
         payment_method = data['payment']
         address_id     = data['address']
         product_Id     = data['productId'] 
         get_total      = data['get_total'] 
         user           = request.session.get('name')
         username       = Usercreation.objects.get(username= user)
         product        = Product.objects.get(id = product_Id)
         address        = CustomerAdress.objects.get(id = address_id ) 
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
        orders      =  Order.objects.filter(user_name = username).order_by('-status')
        cancel_all  = Order.objects.filter (user_name =  username,status = 'Canceled').count()
        return_all  = Order.objects.filter (user_name =  username,status = 'Return').count()
        cartcount   =  OrderItem.objects.filter(user = username).count()
    
    else:   
        error   = "You must log in  for see your account" 
        context = {'form':form,'error':error}
        return render(request,'customer/signin.html',context)
    contex      = {'order_all':order_all,'orders':orders,'cartcount':cartcount,'choices':choices,'user': user,'cancel_all':cancel_all,'return_all':return_all}  
    return render(request,'customer/user_account.html' ,contex)

     
def cart_item_buy_View(request):
     if request.session.get('name'):
         data  = json.loads(request.body)
         payment_method = data['payment']
         address_id     = data['address']
         product_Id     = data['productId'] 
         get_total      = data['get_total']
         user           = request.session.get('name') 
         username       = Usercreation.objects.get(username= user)
         product        = OrderItem.objects.filter(user = username)
         address        = CustomerAdress.objects.get(id = address_id)
         tax = 0
         for i in product:
             tax       =  i.product.product_prize/18   
             get_total =    (i.product.product_prize+tax +40) *i.quantity 
             quantity  = i.quantity 
             print(get_total,"quantity")
             Order( Customer = address, order_product  =i.product,
             user_name = username,payment_method = payment_method,
             quantity  = i.quantity ,total_prize =get_total).save()

             product.delete()


         return JsonResponse('cash-on-delevery for cart items' ,safe=False)





def add_new_address_View(request):
    form  = CustomerAdressForm()
    if request.method == 'POST':
        user1        = request.session.get('name')
        user         = Usercreation.objects.get( username = user1) 
        first_name   =  request.POST['first_name']
        last_name    = 	request.POST['last_name']
        phone_number =	request.POST['phone_number']
        house_name   = 	request.POST['house_name']
        street_name  =	request.POST['street_name'] 
        city         =  request.POST['city']
        state	     =  request.POST['state']
        country	     =  request.POST['country']
        post_code    =  request.POST['post_code']

        CustomerAdress.objects.create(user = user ,first_name = first_name,last_name = last_name
        ,phone_number = phone_number,house_name = house_name
        ,street_name  = street_name,city = city,state = state,country = country,
            post_code = post_code )
        Items         = OrderItem.objects.filter(user = user)
        form          = CustomerAdress.objects.filter(user = user)
        sum           = 0

        for i in Items:
            sum        += i.quantity  * i.product.product_prize
            tax         = int(sum/18)
            grandtotal  = tax+sum+40

        context = {'Items':Items,'form':form,'grandtotal':grandtotal,'tax':tax}  
        return render (request,'customer/checkout.html', context)  

    if request.session.get('name'):
        context  = {'form':form}
        return render (request,'customer/Add_address.html',context)




def add_new_addresforEachOrder_View(request,id):
    form            = CustomerAdressForm() 
    if request.session.get('name'):
        product_id  = Product.objects.filter(id = id)
        context     = {'form':form,'product_id':product_id} 
        return render (request,'customer/Add_address-2.html',context)




def newaddress_save_view(request,id):
     choices = Category.objects.all()
     if request.method == 'POST':
        user1        = request.session.get('name')
        user         = Usercreation.objects.get( username = user1) 
        first_name   =  request.POST['first_name']
        last_name    = 	request.POST['last_name']
        phone_number =	request.POST['phone_number']
        house_name   = 	request.POST['house_name']
        street_name  =	request.POST['street_name'] 
        city         =  request.POST['city']
        state	     =  request.POST['state']
        country	     =  request.POST['country']
        post_code    =  request.POST['post_code']  

        CustomerAdress.objects.create(user = user ,first_name = first_name,last_name = last_name
        ,phone_number = phone_number,house_name = house_name
        ,street_name  = street_name,city = city,state = state,country = country,
            post_code = post_code )

        cartcount  = OrderItem.objects.filter(user = user).count()
        Items      = Product.objects.filter(id = id)
        form       = CustomerAdress.objects.filter(user = user)
        for i in Items:
            tax     = int(( i.product_prize)/18)
            grandtotal = tax+i.product_prize +40 
        context = {'Items':Items,'form':form,'tax':tax,
        'grandtotal':grandtotal,'choices':choices,'cartcount':cartcount} 
        return render (request,'customer/checkout-2.html', context)



def my_profile_view(request):
    choices =Category.objects.all()
    if request.session.get('name'):
        user     = request.session.get('name')
        print(user)
        form     = Usercreation.objects.filter(username = user)
        username = Usercreation.objects.get(username = user)
        address  = CustomerAdress.objects.filter(user =username)
        context  = {'form':form,'address':address,'choices':choices}
        print(address)
        return render(request,'customer/User_profile.html',context)


def delete_address_View(request,id):
     choices    = Category.objects.all()
     if request.session.get('name'):
        user    = request.session.get('name')
        delete_address = CustomerAdress.objects.get(id = id)
        delete_address.delete()
        username  = Usercreation.objects.get(username = user)
        form      = Usercreation.objects.filter(username = user)
        username  = Usercreation.objects.get(username = user)
        address   = CustomerAdress.objects.filter(user =username).order_by('-id')
        cartcount =  OrderItem.objects.filter(user = username).count()
        context   = {'form':form,'address':address,'choices':choices}
        print(address)
        return render(request,'customer/User_profile.html',context)
     else:
         return redirect('/')

 



def add_new_addressfor_userProfile_View(request):
    choices =Category.objects.all()
    form  = CustomerAdressForm() 
    if request.method == 'POST':
        user1 = request.session.get('name')
        user   = Usercreation.objects.get( username = user1) 
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
        cartcount    = OrderItem.objects.filter(user   = user).count()
        form         = Usercreation.objects.filter(username  = user)
        username     = Usercreation.objects.get(username = user)
        address      = CustomerAdress.objects.filter(user = username)
        context      = {'form':form,'address':address,'choices':choices,'cartcount':cartcount}
        print(address)
        return render(request,'customer/User_profile.html',context)
    if request.session.get('name'):
            context = {'form':form} 
            return render (request,'customer/Add_address-3.html',context)
 




def cancel_order_view(request,id):
        if request.session.get('name'):
            choices =Category.objects.all()
            user = request.session.get('name')
            username = Usercreation.objects.get(username = user)
            cancel_or_return = Order.objects.get(id = id)
            if cancel_or_return.status =='Processing' or  cancel_or_return.status == 'Packed': 
                cancel_or_return.status ='Canceled'
                cancel_or_return.save()
            elif cancel_or_return.status == 'Delivered':
                cancel_or_return.status  = 'Return'
                cancel_or_return.save()
            order_all   =  Order.objects.filter(user_name = username).count()
            orders      =  Order.objects.filter(user_name = username).order_by('-id')
            cartcount   =  OrderItem.objects.filter(user = username).count()
            return_all  = Order.objects.filter (user_name =  username,status = 'Return').count()
            cancel_all  = Order.objects.filter (user_name =  username,status = 'Canceled').count()
            contex = {'order_all':order_all,'orders':orders,'cartcount':cartcount,
            'choices':choices,'user': user,'cancel_all':cancel_all,'return_all':return_all} 
            return render(request,'customer/user_account.html' ,contex)

        else:
            return redirect('/')


             
def editprofile_View(request):
    choices =Category.objects.all()
    if request.method  == 'POST':
        user = request.session.get('name')
        user = Usercreation.objects.get(username = user)
        editedform =  Customer(request.POST,instance  = user )
        print('form is get')
        if editedform.is_valid():
            editedform.save() 
            user        = request.session.get('name')
            form        = Usercreation.objects.filter(username = user)
            username    = Usercreation.objects.get(username = user)
            address     =    CustomerAdress.objects.filter(user =username)
            context     = {'form':form,'address':address,'choices':choices}
            return render (request,'customer/User_profile.html',context)
        else:
            print(editedform.errors)
    
    if request.session.get('name'):
        user            = request.session.get('name')
        username        = Usercreation.objects.get(username = user)
        update_form     = Customer(instance  =  username)
        context         = {'update_form':update_form}
        return render(request,'customer/edit_profile.html',context)

    else:
        return redirect('/')


def tracking_order_View(request,id):
    if request.session.get('name'):
        track_order = Order.objects.filter(id = id)
        dt = datetime.now()
        td = timedelta(days=4)
        est_date_delvery = dt + td
        context     = {'track_order':track_order,'est_date_delvery':est_date_delvery}

    return render(request,'customer/track_order.html',context)  