from __future__ import unicode_literals
from builtins import print
from datetime import datetime
from email import message
from email.errors import ObsoleteHeaderDefect
import encodings
import imp
from multiprocessing import context
from turtle import st
from builtins import KeyError, float, int, len, print,str
from venv import create
from xmlrpc.client import DateTime
import pandas as pd
from urllib import request, response
from django import http
from django.shortcuts import render,redirect,get_object_or_404
from django.shortcuts import render,redirect
from httplib2 import RedirectLimit
from sqlalchemy import column
from Dashboard.forms import Update_form
from customer.forms import *
from customer.models import *
from django.core.paginator import Paginator
from django.contrib.auth import authenticate
from customer.forms import *
from Dashboard.forms import * 
from django.core.exceptions import ValidationError
from django.http import HttpResponse, JsonResponse
import csv
import xlwt
from django.contrib import messages


get_page = 5 
# Create your views here.



# ========================================================================================================================================= 
def adminpart(request):
    form = Customer()
    form = Customer(request.POST or None, request.FILES or None)
    if request.method == 'POST':
        adminlogin = authenticate(username = request.POST ['username'],password = request.POST['password1'])
        username = request.POST['username']
        if adminlogin is not None:
            admincheck = Usercreation.objects.get(username = username)
            if admincheck.is_superuser:
                        request.session['name'] = request.POST['username']
                        total_customer  = Usercreation.objects.all().count()
                        total_product   = Product.objects.all().count()
                        total_category  = Category.objects.all().count()
                        total_order     = Order.objects.all().count()
                        cancel_order    = Order.objects.filter(status ='Canceled').count()   
 
                     

                        print(cancel_order)
                        contex          = {'total_product'  : total_product,
                                        'total_customer'    : total_customer,
                                        'total_category'    : total_category,
                                        'total_order'       : total_order,
                                        'cancel_order'      :cancel_order  ,
                                    
                                        }

                        return render(request,'adminpart/dashbord.html',contex)
        
        else:
            errorshowing = 'Incorrect user name and password'
            return render(request,'adminpart/admin_login.html',{'errorshowing': errorshowing,'form':form})

        
    else:
        form = Customer()
        return render(request,'adminpart/admin_login.html',{'form':form })
# ========================================================================================================================================= 

def admin_dashboard(request):
    if request.session.get('name'):
        total_sum =0
        total_customer  = Usercreation.objects.all().count()
        total_product   = Product.objects.all().count()
        total_category  = Category.objects.all().count()
        total_order     = Order.objects.all().count()
        total_earnings  = Order.objects.all()   
        cancel_order     = Order.objects.filter(status ='Canceled').count()  
        delivered_order = Order.objects.filter(status ='Delivered').count()  
        for i  in total_earnings:
            total_sum +=i.total_prize

        print(total_sum)    
        contex        = {'total_product'  : total_product,
                        'total_customer'  : total_customer,
                        'total_category'  : total_category,
                        'total_order'     : total_order,
                        'total_sum'       :total_sum, 
                        'cancel_order'    :cancel_order ,
                         'delivered_order':delivered_order    
                       
                        }
        return render(request,'adminpart/dashbord.html',contex)
    else:
        return redirect('/adminpanel/login/')
  
# ========================================================================================================================================= 




# Fetching user data and displaying, Here using page initions 
def user_view(request):
    if request.session.get('name'):
        page_inition = Paginator(Usercreation.objects.all(),6) 
        page = request.GET.get('page')
        listing = page_inition.get_page(page)
        return render (request,'adminpart/user-management.html',
        {'listing':listing})

    else:
        form = Customer()
        return render(request,'adminpart/admin_login.html',{'form':form })
# ========================================================================================================================================= 

#showing  full details of customer 
def user_view_full_details(request, pk):
    pass
    # full_detials = useraddress.objects.get(id = pk) 
    # context = {'full_detials':full_detials}
    # return render (request,'adminpart/user_view_details.html',context)

# =========================================================================================================================================  
# Fetching products data and displaying

def product_view(request):
    if request.session.get('name'):

        products = Product.objects.all()
        return render(request,'adminpart/product-management.html',{'products':products})
    else:
        return redirect('/adminpanel/login/')    

# =========================================================================================================================================  
# Fetching category and displaying   

def category_view(request):
    if request.session.get('name'):
        categories = Category.objects.all()
        return render(request,'adminpart/category.html',{'categories':categories})
    else:
        return redirect('/adminpanel/login/')    



 # =========================================================================================================================================    
def delete_product(request,id):
    if request.session.get('name'):
        print('ok')
        dumb = Product.objects.get(pk = id)
        dumb.delete()
        return redirect('product_view')
    else:
        return redirect('/adminpanel/login/')    
    

# =========================================================================================================================================      

def update_product(request,id):
    if request.method =='POST':
        data = Product.objects.get(pk = id)
        form = Update_form(request.POST,request.FILES, instance= data)
        if form.is_valid():
            form.save()
            return redirect('product_view')

    else:
        if request.session.get('name'):
            update= Product.objects.get(id = id)
            form = Update_form(instance= update)
            return render(request,'adminpart/update_product.html',{'form':form,'update':update})
        else:
            return redirect('/adminpanel/login/')    


 # ========================================================================================================================================= 

def add_product(request):
    if request.method == 'POST':
        add_data = Update_form(request.POST,request.FILES)
        if add_data.is_valid():
            add_data.save()
            return redirect('product_view')
    else:
        if request.session.get('name'):        
            update=  Update_form()
            return render(request,'adminpart/add_product.html',{'update':update})
        else:
            return redirect('/adminpanel/login/')    
   

# ========================================================================================================================================= 

def userStatusview(request,id):
    if request.session.get('name'):
        status =Usercreation.objects.get(id  = id)
        status.is_active = not(status.is_active)
        status.save()
        return redirect ('usermanagement')
    else:
        return redirect('/adminpanel/login/')    



# ========================================================================================================================================= 

def addcategory_view(request):
    form =Category_form()
    if request.method == 'POST':
                category =Category_form(request.POST)
                if category.is_valid():
                    category.save()
                    return redirect('categorymanagement')           
    else:
        if request.session.get('name'):
            form =Category_form()
            return render(request,'adminpart/AddCategory.html',{'form':form})  
        else:
            return redirect('/adminpanel/login/')     

# ========================================================================================================================================= 


def deletecategory_view(request,id):
    if request.session.get('name'):
        dumb = Category.objects.get(pk = id)
        dumb.delete()
        return redirect ('categorymanagement')
    else:
        return redirect('/adminpanel/login/')



# ========================================================================================================================================= 

def editcategory_view(request,id):
    if request.method == 'POST':
        data= Category.objects.get(pk = id)
        edit_category = Category_form(request.POST,instance=data)
        if edit_category.is_valid():
            edit_category.save()
            return redirect('categorymanagement') 

    else:
        if request.session.get('name'):     
            update= Category.objects.get(id = id)
            contex = Category_form(instance = update)
            return render(request,'adminpart/EditCategory.html',{'contex':contex,'update':update})
        else:
            return redirect('/adminpanel/login/')



# ========================================================================================================================================= 
#Design management view

def designManagement_View(request):
    Design_page = Design.objects.all()

    return render (request,'adminpart/Design_management.html',{'Design_page':Design_page})
# =========================================================================================================================================     

def ordermangemet_view(request):
    if request.session.get('name'):   
        order = Order.objects.all().order_by('-date_ordered')
        contex = {'order':order}
        return render (request, 'adminpart/order-management.html',contex)
    else:
        return redirect('/adminpanel/login/')

# ========================================================================================================================================= 
def edit_status_View(request,id):
    if request.session.get('name'):
        user = request.session.get('name')
        username = Usercreation.objects.get(username = user)
        edit_status = Order.objects.get(id = id)
        print(edit_status)
        if edit_status.status   == 'Processing':
            print(edit_status.status)
            edit_status.status  = "Packed"
         
        elif edit_status.status == 'Packed':
            edit_status.status  = "Delivered"
            date = datetime.now()
            print(date,'//////////////////////////////////')
            Order.objects.update(user_name = username ,date_delivered = date)
        edit_status.save()         
        return redirect ('/adminpanel/order_management')
# =========================================================================================================================================         

def coupen_management_View(request):
    if request.session.get('name'):
        coupen  = Coupen.objects.all()
        context = {'coupen':coupen}
        return render(request,'adminpart/coupen-management.html',context)

# ========================================================================================================================================= 
       



def edit_coupen_View(request,id):
    if request.session.get('name'):
        if request.method == 'POST':
            data= Coupen.objects.get(pk = id)
            form = CoupenForm(request.POST,instance = data )
            if form.is_valid():
                form.save()
                return redirect('/adminpanel/coupen_management')

        else:
            update= Coupen.objects.get(id = id)           
            edit = Coupen.objects.get(id = id)
            form = CoupenForm(instance= edit)
            contex = {'form':form,'update':update}
    
            return render (request,'adminpart/edit_coupen.html',contex)
    else :
        return redirect('adminpanel/login')
# =========================================================================================================================================         

def delete_coupen_view(request,id):
    delete_coupen = Coupen.objects.get(id = id)
    delete_coupen.delete()
    return redirect('/adminpanel/coupen_management')


def add_coupen_View(request):
     if request.session.get('name'):
        if request.method == 'POST':
           
            form  = CoupenForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('/adminpanel/coupen_management')

        else:
            form   = CoupenForm()
            contex = {'form':form}
    
            return render (request,'adminpart/add_coupen.html',contex)
     else:
         return redirect('adminpanel/login')
def cancel_status_view(request,id):
    cancel_status = Order.objects.get(id = id)        
    cancel_status.status = "Canceled"
    cancel_status.save()
    return redirect('/adminpanel/order_management')

# ========================================================================================================================================= 


def sales_report_view(request):
    if request.session.get('name'):
        Items   = Order.objects.all()

        context = {'Items':Items}
        return render(request,'adminpart/sales_reports.html',context)

# ========================================================================================================================================= 


def export_as_excel_view(request):
    if request.session.get('name'):
        response == HttpResponse(content_type = 'application/ms-excel')
        d = datetime.strptime(datetime.date, '%Y-%m-%d %H:%M:%S')
        response['content-Disposition'] = 'attachment; filename = Expenses' + \
            str(datetime.now()) +'.xls'
        wb  = xlwt.Workbook(encoding = 'utf-8')
        ws =  wb.add_sheet('Expenses')
        row_num  = 0
        font_style  = xlwt.XFStyle()
        font_style.font.b = old=True
        columns  = ['user_name','order_product','quantity','total_prize','Date order','transcation_id']
        for col_num in  range(len(column)):
            ws.write(row_num,col_num,columns[col_num],font_style)
        font_style.font.bold  = True

        rows  = Order.objects.all().values_list('user_name','order_product','quantity','total_prize','Date order','transcation_id')
        for row in rows:
            row_num += 1
            for col_num in range(len(row)):
                ws.write(row_num,col_num,str(row[col_num]),font_style)

        ws.save(response)
        return response




# ========================================================================================================================================= 

def offer_management_view(requst):
    if request.session.get('name'):
        # product_offer  = ProductOffer.objects.all()
        # category_offer = categoryOffer.objects.all()
        # context        = {'product_offer':product_offer,'category':category_offer}

        return render (request ,'adminpanel/offer_management')
    else:
        return redirect('/adminpanel/login/')   

#=========================================================================================================================================         

def date_wise_report_view(request):
    if request.session.get('name'):
        if request.method == 'GET':
            date    = request.GET['date']
            month   = request.GET['month']
            year    = request.GET['year']
         
            if date  == '' and month == '' and year == '':
                   messages.error(request,'Empty result, fill the above field')
                   return redirect('/adminpanel/sales_report/')
            else:
                global result
                if date  != '':
                    result= Order.objects.filter(date_ordered =date)

                elif month  != '': 
                
                    month = month.split('-')
                    print(month[1])
                    result= Order.objects.filter(date_ordered__month = month[1])
                elif year != '':
                    year = year.split('-')
                    print(year[0])
                    result= Order.objects.filter(date_ordered__year = year[0])

                context = {'result':result}
                return render (request,'adminpart/sale_report2.html',context)
                    


                 
               
#=========================================================================================================================================          




def adminlogout_view(request):

    del request.session['name']

    return redirect('/adminpanel/login/')
       