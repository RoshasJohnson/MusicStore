import imp
from multiprocessing import context
from unicodedata import category
from urllib import request
from django.shortcuts import render,redirect,get_object_or_404
from django.shortcuts import render,redirect
from httplib2 import RedirectLimit
from Dashboard.forms import Update_form
from customer.forms import *
from customer.models import *
from django.core.paginator import Paginator
from django.contrib.auth import authenticate
from customer.forms import *
from Dashboard.forms import * 
from django.core.exceptions import ValidationError
 

get_page = 5 
# Create your views here.




# --------------------------------------------------------------------
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
                        contex          = {'total_product'  : total_product,
                                        'total_customer'  : total_customer,
                                        'total_category'  : total_category,
                                        'total_order'     : total_order,
                                    
                                        }

                        return render(request,'adminpart/dashbord.html',contex)
        
        else:
            errorshowing = 'Incorrect user name and password'
            return render(request,'adminpart/admin_login.html',{'errorshowing': errorshowing,'form':form})

        
    else:
        form = Customer()
        return render(request,'adminpart/admin_login.html',{'form':form })

# --------------------------------------------------------------------
def admin_dashboard(request):
    if request.session.get('name'):
        total_sum =0
        total_customer  = Usercreation.objects.all().count()
        total_product   = Product.objects.all().count()
        total_category  = Category.objects.all().count()
        total_order     = Order.objects.all().count()
        total_earnings  = Order.objects.all()   
        for i  in total_earnings:
            total_sum +=i.total_prize

        print(total_sum)    
        contex        = {'total_product'  : total_product,
                        'total_customer'  : total_customer,
                        'total_category'  : total_category,
                        'total_order'     : total_order,
                        'total_sum'       :total_sum,  
                       
                        }
        return render(request,'adminpart/dashbord.html',contex)
    else:
        return redirect('/adminpanel/login/')
  
# --------------------------------------------------------------------




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
# --------------------------------------------------------------------

#showing  full details of customer 
def user_view_full_details(request, pk):
    pass
    # full_detials = useraddress.objects.get(id = pk) 
    # context = {'full_detials':full_detials}
    # return render (request,'adminpart/user_view_details.html',context)

# -------------------------------------------------------------------- 
# Fetching products data and displaying

def product_view(request):
    if request.session.get('name'):
        page_inition = Paginator(Product.objects.all(),4)
        page = request.GET.get('page')
        products =page_inition.get_page(page)
        return render(request,'adminpart/product-management.html',{'products':products})
    else:
        return redirect('/adminpanel/login/')    

# -------------------------------------------------------------------- 
# Fetching category and displaying   

def category_view(request):
    if request.session.get('name'):
        categories = Category.objects.all()
        return render(request,'adminpart/category.html',{'categories':categories})
    else:
        return redirect('/adminpanel/login/')    



 # --------------------------------------------------------------------   
def delete_product(request,id):
    if request.session.get('name'):
        print('ok')
        dumb = Product.objects.get(pk = id)
        dumb.delete()
        return redirect('product_view')
    else:
        return redirect('/adminpanel/login/')    
    

# --------------------------------------------------------------------     

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


 # ------------------------------------------------------------------------------------------  

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
   



def userStatusview(request,id):
    if request.session.get('name'):
        status =Usercreation.objects.get(id  = id)
        status.is_active = not(status.is_active)
        status.save()
        return redirect ('usermanagement')
    else:
        return redirect('/adminpanel/login/')    




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




def deletecategory_view(request,id):
    if request.session.get('name'):
        dumb = Category.objects.get(pk = id)
        dumb.delete()
        return redirect ('categorymanagement')
    else:
        return redirect('/adminpanel/login/')




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



#------------------------------------------------------------------------------------------------------------
#Design management view

def designManagement_View(request):
    Design_page = Design.objects.all()

    return render (request,'adminpart/Design_management.html',{'Design_page':Design_page})

def ordermangemet_view(request):
    if request.session.get('name'):   
        order = Order.objects.all().order_by('-date_ordered')
        contex = {'order':order}
        return render (request, 'adminpart/order-management.html',contex)
    else:
        return redirect('/adminpanel/login/')



def edit_status_View(request,id):
    if request.session.get('name'):
        user = request.session.get('name')
        username = Usercreation.objects.get(username = user)
        edit_status = Order.objects.get(id = id)
        print(edit_status)
        if edit_status.status   == 'Processing':
            print(edit_status.status)
            edit_status.status  = "Packed"
            print(edit_status.status,'fds')
        elif edit_status.status == 'Packed':
            edit_status.status  = "Delivered"
        edit_status.save()         
        return redirect ('/adminpanel/order_management')

def coupen_management_View(request):
    if request.session.get('name'):
        coupen  = Coupen.objects.all()
        context = {'coupen':coupen}
        return render(request,'adminpart/coupen-management.html',context)




    
#log out admin_----------------------------------------------------------------------------------------------- 


def adminlogout_view(request):
    del request.session['name']
    
    return redirect('/adminpanel/login/')
      