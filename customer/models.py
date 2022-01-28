from enum import auto
from itertools import product
from re import T
from tkinter.tix import Tree
from django.db import models
from django.contrib.auth.models import AbstractUser
from django import forms
from django.utils import timezone
from sqlalchemy import false, true
import os
from twilio.rest import Client
# from customer.forms import Customer

# Create your models here.
class Usercreation(AbstractUser):
    phone_number = models.CharField(max_length=50)


# --------------------------------   

 

#Choice field for category
class Category(models.Model):
    category_name = models.CharField(max_length=200)

    def __str__(self):
        return self.category_name

    class Meta:
        db_table = ''
        managed = True
        verbose_name =  'category'
        verbose_name_plural =  'categorys'


# _______________________________________


# created product table
class Product(models.Model):
    product_name        = models.CharField(max_length=200, null = True)
    product_description = models.TextField(max_length=10000, null = True)
    product_prize       =  models.FloatField(max_length=200, null = True)
    stock               = models.IntegerField(max_length=200,null= True)
    is_available        = models.BooleanField(default=True)
    digital             = models.BooleanField(default=False,null= True,blank = True)
    category_type       = models.ForeignKey(Category,on_delete=models.CASCADE,null = True)
    product_image       = models.ImageField(null= True,blank = True,upload_to ='images/')
    product_image1      = models.ImageField(null= True,blank = True,upload_to ='images/')
    product_image2      = models.ImageField(null= True,blank = True,upload_to ='images/')
    product_image3      = models.ImageField(null= True,blank = True,upload_to ='images/')
   
    def __str__(self):
        return self.product_name
         
 
    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Product'
        verbose_name_plural = 'Products' 




# ______________________________________________________

#created category table   
class useraddress(models.Model):
    full_name       = models.CharField(max_length=200, default="",editable=False)
    house_address   = models.CharField(max_length=200, null = True)
    post_code       = models.IntegerField(max_length=200, null = True)
    city            = models.CharField(max_length=200, null = True)
    state           = models.CharField(max_length=200, null = True)
    country         = models.CharField(max_length=200, null = True)
    


    def __str__(self):
        return str(self.user_name)

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'useradress'
        verbose_name_plural = 'useradresss'



class Sms(models.Model):
    result = models.PositiveIntegerField(max_length=4)

    def __str__(self):
        return str(self.result)
        
    



class Design(models.Model):
    Icon_image    = models.ImageField(null= True,blank = True,upload_to ='images/')
    Logo_image    = models.ImageField(null= True,blank = True,upload_to ='images/')
    Banner_image1 = models.ImageField(null= True,blank = True,upload_to ='images/')
    Banner_image2 = models.ImageField(null= True,blank = True,upload_to ='images/')
    Banner_image3 = models.ImageField(null= True,blank = True,upload_to ='images/')
    Footer_image  = models.ImageField(null= True,blank = True,upload_to ='images/')
    
    def __str__(self):
        return str(self.Icon_image)




# class Cart(models.Model):
#     user_id = models.ForeignKey(Usercreation, on_delete=models.CASCADE)
#     category_id = models.ForeignKey(Category, on_delete=models.CASCADE)
#     quantity = models.BigIntegerField(default=1)
#     subtotal = models.BigIntegerField(default=1)
#     class Meta:
#         db_table = "Cart"



# class CartItem(models.Model):
#     product     = models.ForeignKey(Product,on_delete=models.CASCADE)
#     cart        = models.ForeignKey(Cart,on_delete=models.CASCADE)
#     quantity    = models.IntegerField()
#     is_active   = models.BooleanField(default= True)

#     def __str__(self):
#         return str(self.product)



class Order(models.Model):
    Customer        =  models.ForeignKey(Usercreation,on_delete= models.SET_NULL, null = True ,blank = True )
    date_ordered    =  models.DateField(auto_now_add= True)
    complete        =  models.BooleanField(default= False,null = True ,blank = True )
    transcation_id  =  models.CharField(max_length=100,null= True)   
    def __str__(self) :
        return str(self.id)  

    @property
    def get_cart_total(self):
        orderitems = self.orderitem_set.all()
        total      = sum([item.get_total for item in orderitems])
        return total
    @property
    def get_cart_items(self):
        orderitems = self.orderitem_set.all()
        total      = sum([item.quantity for item in orderitems])
        return total
    @property
    def shipping(self):
        shipping  = False
        orderItmes = self.OrderItem_set.all()
        
        for i in orderItmes:
            if i.product.digital  == False :
                shipping = True 
        return self.shipping
        
 
class OrderItem(models.Model):
    product     = models.ForeignKey(Product,on_delete= models.SET_NULL, null= True ,blank = True)
    order       = models.ForeignKey(Order,on_delete= models.SET_NULL,blank = True, null= True)  
    quantity    = models.IntegerField(default=0,null = True ,blank= True)
    date_added  = models.DateField(auto_now_add=True)
    
    @property
    def get_total(self):
        total =self.product.product_prize * self.quantity
        return total



 

class ShippingAddress(models.Model):
    customer        = models.ForeignKey(Usercreation,on_delete = models.SET_NULL,blank = True, null= True) 
    order           = models.ForeignKey(Order,on_delete = models.SET_NULL,blank = True, null= True) 
    address         = models.CharField(max_length=200, null = True)
    city            = models.CharField(max_length=200, null = True)
    state           = models.CharField(max_length=200, null = True)
    zipcode         = models.CharField(max_length=200, null = True)
    date_added      = models.DateField(auto_now_add=True)
    def __str__(self) :
        return self.address
    

    

   