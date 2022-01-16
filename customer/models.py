from django.db import models
from django.contrib.auth.models import AbstractUser
from django import forms
from django.utils import timezone
from sqlalchemy import true

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
    product_description = models.CharField(max_length=1000, null = True)
    product_prize     =  models.FloatField(max_length=200, null = True)
    category_type   = models.ForeignKey(Category,on_delete=models.CASCADE,null = True)
    stock           = models.IntegerField(max_length=200,default = 0)
    product_image = models.FileField(null= True,blank = True,upload_to ='images/')
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





        