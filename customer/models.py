
from builtins import int, property, sum
from locale import str
import email
from enum import auto

from builtins import KeyError, float, int, len, print,str
from re import T
from tkinter import CASCADE
from tkinter.tix import Tree

from django.db import models
from django.contrib.auth.models import AbstractUser
from django import forms
from django.utils import timezone
from sqlalchemy import false, null, true
import os
from twilio.rest import Client
import uuid
# from customer.forms import Customer

# Create your models here.
class Usercreation(AbstractUser):
    phone_number = models.CharField(max_length=50)
    coupen       = models.CharField(max_length=50 ,null=True)  
    
# --------------------------------   
class Coupen(models.Model):
    
    Coupencode   = models.IntegerField(max_length=200, null = True,blank = True)
    Coupen_offer = models.IntegerField(max_length=200,null = True)
    
    def __str__(self):
        return str(self.Coupencode)
       
    

#Choice field for category
class Category(models.Model):
   
    category_name   =  models.CharField(max_length=200)
    Category_offer  =  models.IntegerField(max_length=200, null = True)

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
    product_prize       = models.IntegerField(max_length=200, null = True)
    stock               = models.IntegerField(max_length=200,null= True)
    is_available        = models.BooleanField(default=True)
    category_type       = models.ForeignKey(Category,on_delete=models.CASCADE,null = True)
    product_offer       = models.IntegerField(max_length=200,null= True,default=0)
    product_image       = models.ImageField(null= True,blank = True,upload_to ='images/')
    product_image1      = models.ImageField(null= True,blank = True,upload_to ='images/')
    product_image2      = models.ImageField(null= True,blank = True,upload_to ='images/')
    product_image3      = models.ImageField(null= True,blank = True,upload_to ='images/')
    def __str__(self):
        return self.product_name
         
 
    @property
    def get_Total_prize(self):
        tax             = 18 
        shipping_charge = 40
        total_prize = int((self.get_coupen_offer_prize  ) /tax) + int((self.get_coupen_offer_prize  ) +shipping_charge)
        return total_prize


    @property
    def get_coupen_offer_prize(self):
        if self.product_offer == 0:
            coupen_offer_prize = self.product_prize         
        elif self.product_offer > self.category_type.Category_offer:  
            coupen_offer_prize    = int(self.product_prize)  - int((self.product_prize) * int((self.product_offer))/100)
        else:
            coupen_offer_prize    = int(self.product_prize)  - int((self.product_prize) * int((self.category_type.Category_offer))/100)            
        return coupen_offer_prize
     


#created category table   

    


  

class CustomerAdress(models.Model):
    user            = models.ForeignKey(Usercreation,on_delete=models.CASCADE,null = True)
    first_name       = models.CharField(max_length=200)
    last_name       = models.CharField(max_length=200)
    email            = models.EmailField( max_length=254)
    phone_number    = models.CharField(max_length=99)
    house_name      = models.CharField(max_length=200, null = True)
    street_name      = models.CharField(max_length=200, null = True)
    city            = models.CharField(max_length=200, null = True)
    state           = models.CharField(max_length=200, null = True)
    country         = models.CharField(max_length=200, null = True)
    post_code       = models.IntegerField(max_length=200, null = True)


    def __str__(self):
        return str(self.user)

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'CustomerAdress'
        verbose_name_plural = 'CustomerAdress'

  

class Design(models.Model):
    Icon_image    = models.ImageField(null= True,blank = True,upload_to ='images/')
    Logo_image    = models.ImageField(null= True,blank = True,upload_to ='images/')
    Banner_image1 = models.ImageField(null= True,blank = True,upload_to ='images/')
    Banner_image2 = models.ImageField(null= True,blank = True,upload_to ='images/')
    Banner_image3 = models.ImageField(null= True,blank = True,upload_to ='images/')
    Footer_image  = models.ImageField(null= True,blank = True,upload_to ='images/')
    
    def __str__(self):
        return str(self.Icon_image)



STATUS_CHOICES = {
   
    ("Packed" , "Packed"),
    ("Delivered" , "Delivered"),
    ("Canceled" , "Canceled"),
    ("Return", "Return"),

}
class Order(models.Model):
    user_name       = models.ForeignKey(Usercreation,on_delete= models.SET_NULL, null = True ,blank = True )
    Customer        = models.ForeignKey(CustomerAdress,on_delete= models.SET_NULL, null = True ,blank = True )
    date_ordered    = models.DateField(auto_now_add= True)
    status          = models.CharField(choices=STATUS_CHOICES,max_length=100,default='Processing')
    order_product   = models.ForeignKey(Product,on_delete=models.SET_NULL,null=True)
    transcation_id  = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    payment_method  = models.CharField(max_length=10,null= True )
    total_prize     = models.IntegerField( null = True ,blank= True)
    quantity        = models.IntegerField(default=1,null = True ,blank= True)
   
    
    def __str__(self):
         return str(self.user_name)
       

    def order_total(self):
        total_prize  = self.order_product.get_coupen_offer_prize *  self.quantity
        return total_prize
 
    # @property
    # def get_cart_total(self):
    #     orderitems = self.orderitem_set.all()
    #     total      = sum([item.get_total for item in orderitems])
    #     return total
    # @property
    # def get_cart_items(self):
    #     orderitems = self.orderitem_set.all()
    #     total      = sum([item.quantity for item in orderitems])
    #     return total
    # @property
    # def shipping(self):
    #     shipping  = False
    #     orderItmes = self.OrderItem_set.all()
        
    #     for i in orderItmes:
    #         if i.product.digital  == False :
    #             shipping = True 
    #     return self.shipping
        




class OrderItem(models.Model):
    user         = models.ForeignKey(Usercreation,on_delete= models.SET_NULL, null= True ,blank = True) 
    product     = models.ForeignKey(Product,on_delete= models.SET_NULL, null= True ,blank = True)
    quantity    = models.IntegerField(default=1,null = True ,blank= True)
    date_added  = models.DateField(auto_now_add=True)
    
    @property
    def get_total(self): 
        total =self.product.get_coupen_offer_prize * self.quantity
        return total
    @property    
    def get_cart_total(self):
        orderitems = self.orderitem_set.all()
        total      = sum([item.get_total for item in orderitems])
        return total


 

# class ShippingAddress(models.Model):
#     customer        = models.ForeignKey(Usercreation,on_delete = models.SET_NULL,blank = True, null= True) 
#     order           = models.ForeignKey(Order,on_delete = models.SET_NULL,blank = True, null= True) 
#     address         = models.CharField(max_length=200, null = True)
#     city            = models.CharField(max_length=200, null = True)
#     state           = models.CharField(max_length=200, null = True)
#     zipcode         = models.CharField(max_length=200, null = True)
#     date_added      = models.DateField(auto_now_add=True)
#     def __str__(self) :
#         return self.address
    

    

    