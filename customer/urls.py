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
    path('ordering/<int:id>/',views.OrderView,name = 'ordering'),
    path('cart_qty/', views.addcartQtyView,name = 'cart_qty'),
    path('checking_address',views.checkingaddressview,name = 'checking_address') ,
    path('products/<int:id>/',views.productpage_View,name = "products"),
    path('order_placing/',views.order_placingView ,name ="order_placing"),
    path('manage_account',views.user_account_View,name = "manage_account"),
    path('cart_items/',views.cart_item_buy_View,name= "cart_items"),
    path('address',views. add_new_address_View,name = 'address'),
    path('new_address/<int:id>/',views.add_new_addresforEachOrder_View,name = 'new_address'),
    path('new_address_adding/<int:id>/',views.newaddress_save_view,name = "new_address_adding"),
    path('my_profile',views.my_profile_view, name = "my_profile"),
    path('delete_address/<int:id>/',views.delete_address_View,name = "delete_address"),
    path('add_new_address',views.add_new_addressfor_userProfile_View,name = "add_new_address"),
    path('cancel_order/<int:id>/',views.cancel_order_view,name = "cancel_order"),
    path('edit_profile',views.editprofile_View,name = 'edit_profile'),
    path('tracking_order/<int:id>/',views.tracking_order_View,name = "tracking_order")
    ] 