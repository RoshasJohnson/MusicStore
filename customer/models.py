from re import T
from django.db import models
from django.contrib.auth.models import AbstractUser
from django import forms
from django.utils import timezone
from sqlalchemy import true
import os
from twilio.rest import Client

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
    user_name       = models.ForeignKey(Usercreation,on_delete=models.CASCADE,null = True)
    full_name       = models.CharField(max_length=200, null = True)
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




class Cart(models.Model):

    cart_id     = models.CharField(max_length=250,blank= True)
    date_added  = models.DateField(auto_now_add=True) 
    def __str__(self) :
        return self.cart_id
class CartItem(models.Model):
    product     = models.ForeignKey(Product,on_delete=models.CASCADE)
    cart        = models.ForeignKey(Cart,on_delete=models.CASCADE)
    quantity    = models.IntegerField()
    is_active   = models.BooleanField(default= True)
    def __str__(self):
        return str(self.product)

