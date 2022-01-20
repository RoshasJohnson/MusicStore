from curses import panel
from unicodedata import name
from django.urls import path
from.import views

# coding patterns here

urlpatterns = [
    path('login/',views.adminpart, name = 'login'),
    path('',views.admin_dashboard, name ='adminpanel'),
    path('usermanagement/',views.user_view ,name='usermanagement'),
    # path('viewfull/<int:pk>/',views.user_view_full_details,name = 'viewfull'),
     path('productmanagement/',views.product_view,name='product_view'),
    path('categorymanagement/',views.category_view,name='categorymanagement'),
    path('delete_product/<int:id>/',views.delete_product,name= 'delete_product'),
    path('update_product/<int:id>/',views.update_product, name = 'update_product'),
    path('add_product/',views.add_product, name = 'add_product'),
    path('userstatus/<id>/',views.userStatusview,name = 'userstatus'),
    path('addcategory/',views.addcategory_view,name = 'addcategory'), 
    path('deletecategory/<int:id>/',views.deletecategory_view,name = 'deletecategory'),
    path('editcategory/<int:id>/',views.editcategory_view,name ='editcategory'),



    path('design_management/',views.designManagement_View,name = 'design_management'),
    path('admin_logout/',views.adminlogout_view,name = 'admin_logout')
]