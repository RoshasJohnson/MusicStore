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
from urllib.request import Request
from venv import create
from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect, render
import re
from django.views.decorators.csrf import csrf_protect

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
                request.session['name'] = request.POST['username']
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
        user = request.session.get('name')
        print(user)
        Designpage= Design.objects.all()
        customer = request.session.get('name')
        user     = Usercreation.objects.get(username = customer)
        everyproduct = Product.objects.all()
        choices =Category.objects.all() 
        cartcount=  OrderItem.objects.filter(user = user  ).count()
      
        contex = {'everyproduct':everyproduct,
        'Designpage':Designpage,
        'choices':choices,
        'cartcount':cartcount}
        return render(request,'customer/index.html',contex)

    else:
         
        Designpage = Design.objects.all()
        everyproduct = Product.objects.all()
        choices =Category.objects.all()
        order=  OrderItem.objects.all().count()
        print(order,'////////////////////fffffffffffffffffffffffff///////////////////////')
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
        # order,create = Order.objects.update_or_create(Customer = customer,complete =  False)
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
        # order,create = Order.objects.get_or_create(Customer = user,complete =  False)
        Items  = OrderItem.objects.filter(user = user)
        form = CustomerAdress.objects.filter(user = user)
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
    contex = {'Items':Items,'choices':choices,'form':form,'tax':tax,'grandtotal':grandtotal}  
    return render(request,'customer/checkout.html',contex)




 
 
 
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
        # if   OrderItem.objects.filter(product = product).exists():
        #     products =  OrderItem.objects.filter(id = productId)
        #     print(products)
        #     products.quantity  =(products.quantity  + 1)
             
        # else: 
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
    if request.session.get('name'):
        user = request.session.get('name')   
        Items = Product.objects.filter(id = id)
        user1  = Usercreation.objects.get(username = user)
        print(user1,'userrrrrrrrrrrrrrrrrrrrrrrrrrrrr')
        form = CustomerAdress.objects.filter(user = user1)
        
        for i in Items:
            tax =int(( i.product_prize)/18)
            grandtotal  = tax+i.product_prize +40 
           
        context = {'Items':Items,'form':form,'tax':tax,'grandtotal':grandtotal}
        print(grandtotal)
        return render(request,'customer/checkout-2.html',context) 
   
def Blah(request): 
    if request.method == 'GET':
        if 'cod' in request.GET:
        # TypeofPayment  = request.POST.ge t['value']
        # print(TypeofPayment,'fddddddddddddd')
             print('successssssssssssssssssssssssssssssssssssssssssss')
             return redirect ('home/')
    else :
        return HttpResponse ('home/')
  
 
def addcartQtyView(request):
    if request.session.get('name'):
        data  = json.loads(request.body)
        action = data['action']
        productid = data['productId']
        print(action,'rrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrr')
        print(productid,'rrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrr')
        orderItem = OrderItem.objects.get(id  = productid)
        if action == 'add':
            # orderItem = 
            orderItem.quantity =(orderItem.quantity  + 1)
        elif action == 'remove':
            orderItem.quantity =(orderItem.quantity  - 1)
            orderItem.delete()
            # order.delete()
        if productid in data:    
            orderItem = OrderItem.objects.get(id = productid)
        orderItem.save()

        if orderItem.quantity <= 0:
           orderItem.delete()
        return JsonResponse('ddddd', safe = False) 
   


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
        pass

        
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
         user = request.session.get('name')
         username = Usercreation.objects.get(username= user)
         product   = Product.objects.get(id = product_Id)
         address   = CustomerAdress.objects.get(id = address_id ) 
         print(address,'address')
         print(payment_method,address,'hheeheheheheheheehhe')

         
         Order.objects.create( Customer = address,order_product =product,
         user_name = username,payment_method = payment_method ,total_prize =get_total)
         return JsonResponse('cash on delery', safe = False) 
   
        

def user_account_View(request):
    form = Customer()
    if request.session.get('name'):
        user    = request.session.get('name')
        username = Usercreation.objects.get(username  = user)
        order_all = Order.objects.filter(user_name = username).count()
      
        contex = {'order_all':order_all}
        return render(request,'customer/user_account.html' ,contex)
    else:
        error = "You must log in  for see your account"
        context = {'form':form,'error':error}
        return render(request,'customer/signin.html',context)

    
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
             