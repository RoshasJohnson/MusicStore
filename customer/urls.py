from unicodedata import name
from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.homepage_view,name='homepage_view'),
    path('usersignup/',views.usersignupView,name = 'usersignup'),
    path('signin/',views.signIcon_view,name = 'signin/'),
    path('registeruser/',views.register_USer_View,name= 'registeruser/'),
    path('selected_Product/<int:id>',views.selected_Product_view,name = 'selected_Product'),
    path('cart/',views.cart_View,name = 'cart'),
    path('add_cart/<int:id>',views.addto_cart_View,name = 'add_cart')

]

