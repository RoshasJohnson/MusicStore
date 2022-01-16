import imp
from django.shortcuts import render,redirect,get_object_or_404
from django.shortcuts import render,redirect
from Dashboard.forms import Update_form
from customer.forms import *
from customer.models import *
from django.core.paginator import Paginator
from django.contrib.auth import authenticate
from customer.forms import *



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
                return render(request,'adminpart/dashbord.html')
        
        else:
            errorshowing = 'Incorrect user name and password'
            return render(request,'adminpart/admin_login.html',{'errorshowing': errorshowing,'form':form})

        
    else:
        form = Customer()
        return render(request,'adminpart/admin_login.html',{'form':form })

# --------------------------------------------------------------------
def admin_dashboard(request):

    return render(request,'adminpart/dashbord.html')

# --------------------------------------------------------------------




# Fetching user data and displaying, Here using page initions 
def user_view(request):
    # dataset = Usercreation.objects.all()
    page_inition = Paginator(Usercreation.objects.all(),6) 
    page = request.GET.get('page')
    listing = page_inition.get_page(page)
    return render (request,'adminpart/user-management.html',
    {'listing':listing})   



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
    page_inition = Paginator(Product.objects.all(),5)
    page = request.GET.get('page')
    products =page_inition.get_page(page)

    

    return render(request,'adminpart/product-management.html',{'products':products})

# -------------------------------------------------------------------- 
# Fetching category and displaying   

def category_view(request):
    categories = Category.objects.all()
    return render(request,'adminpart/category.html',{'categories':categories})    



 # --------------------------------------------------------------------   
def delete_product(request,id):
    print('ok')
    dumb = Product.objects.get(pk = id)
    dumb.delete()
    return redirect('product_view')

# --------------------------------------------------------------------     

def update_product(request,id):
    if request.method =='POST':
        data = Product.objects.get(pk = id)
        form = Update_form(request.POST, instance= data)
        if form.is_valid():
            form.save()
            return redirect('product_view')

    else:
        update= Product.objects.get(pk = id)
        form = Update_form(instance= update)
        return render(request,'adminpart/update_product.html',{'form':form,'update':update})


 # ------------------------------------------------------------------------------------------  

def add_product(request):
    if request.method == 'POST':
        add_data = Update_form(request.POST,request.FILES)
        if add_data.is_valid():
            add_data.save()
            return redirect('product_view')
    else:        
        update=  Update_form()
        return render(request,'adminpart/add_product.html',{'update':update})
   


