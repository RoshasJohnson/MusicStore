from unicodedata import name
from django.urls import path,include
from . import views
from.views import checkout_view, inclusiontag


urlpatterns = [
    path('',views.homepage_view,name='homepage_view'),
    path('inctag', inclusiontag),
    path('usersignup/',views.usersignupView,name = 'usersignup'),
    path('signin/',views.signIcon_view,name = 'signin/'),
    path('registeruser/',views.register_USer_View,name= 'registeruser/'),
    path('selected_Product/<int:id>',views.selected_Product_view,name = 'selected_Product'),
    path('cart/',views.cart_View,name = 'cart'),
    # path('add-to-cart',views.addto_cart_View,name = 'add-to-cart'),
    path('update_item/',views.updateItem, name= 'update_item'),
    path('check_out',views.checkout_view,name  = 'check_out'),
    path('place_order/',views.place_orderView, name= 'place_order'),
    path('proccesing_order/',views.Process_orderView,name = 'proccesing_order'),
    path('ordering/<int:id>/',views.BuyView,name = 'ordering'),
     path('placing_order/',views.Blah,name = 'placing_order'),
    path('cart_qty/', views.addcartQtyView,name = 'cart_qty'),
    path('checking_address',views.checkingaddressview,name = 'checking_address') 
    ]