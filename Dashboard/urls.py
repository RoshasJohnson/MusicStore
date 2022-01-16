from django.urls import path,include
from.import views

urlpatterns = [
    path('',views.adminpart, name = 'adminpart'),
    path('usermanagement/',views.user_view ,name='usermanagement'),
    # path('viewfull/<int:pk>/',views.user_view_full_details,name = 'viewfull'),
     path('productmanagement/',views.product_view,name='product_view'),
    path('categorymanagement/',views.category_view,name='category_view'),
    path('delete_product/<int:id>/',views.delete_product,name= 'delete_product'),
    path('update_product/<int:id>/',views.update_product, name = 'update_product'),
    path('add_product/',views.add_product, name = 'add_product')
  
]