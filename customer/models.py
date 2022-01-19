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
    product_name       = models.CharField(max_length=200, null = True)
    product_description = models.CharField(max_length=10000, null = True)
    product_prize     =  models.FloatField(max_length=200, null = True)
    stock           = models.IntegerField(max_length=200,default = 0)
    category_type   = models.ForeignKey(Category,on_delete=models.CASCADE,null = True)
    product_image = models.ImageField(null= True,blank = True,upload_to ='images/')
    product_image1 = models.ImageField(null= True,blank = True,upload_to ='images/')
    product_image2 = models.ImageField(null= True,blank = True,upload_to ='images/')
    product_image3 = models.ImageField(null= True,blank = True,upload_to ='images/')
   
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
    user_name = models.ForeignKey(Usercreation,on_delete=models.CASCADE,null = True)
    full_name = models.CharField(max_length=200, null = True)
    house_address = models.CharField(max_length=200, null = True)
    post_code = models.IntegerField(max_length=200, null = True)
    city = models.CharField(max_length=200, null = True)
    state = models.CharField(max_length=200, null = True)
    country = models.CharField(max_length=200, null = True)
    


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
        
    

    def save(self,*args, **kwargs):
        if self.result < 20 :
            account_sid = os.environ['AC0eb31c976dfd6b92c07d3e35d715b3f8']
            auth_token = os.environ['a8301a295d3b125452c6559da1a24a78']
            client = Client(account_sid, auth_token)

            message = client.messages \
                .create(
                    messaging_service_sid='+19378844760',
                    body='this is working',
                    to='7012598205'
                )

            print(message.sid)
            
        return super().save(*args, **kwargs)



class Design(models.Model):
    Icon_image = models.ImageField(null= True,blank = True,upload_to ='images/')
    Logo_image = models.ImageField(null= True,blank = True,upload_to ='images/')
    Banner_image1 = models.ImageField(null= True,blank = True,upload_to ='images/')
    Banner_image2 = models.ImageField(null= True,blank = True,upload_to ='images/')
    Banner_image3 = models.ImageField(null= True,blank = True,upload_to ='images/')
    Footer_image =models.ImageField(null= True,blank = True,upload_to ='images/')

