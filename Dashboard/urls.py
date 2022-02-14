
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
    path('admin_logout/',views.adminlogout_view,name = 'admin_logout'),
    path('order_management',views.ordermangemet_view,name = "order_management"),
    path('edit_status/<int:id>/',views.edit_status_View,name = "edit_status"),
    path('coupen_management',views.coupen_management_View,name = 'coupen_management'),
    path('edit_coupen/<int:id>/',views.edit_coupen_View, name = 'edit_coupen'),
    path('delete_coupen/<int:id>/',views.delete_coupen_view,name = 'delete_coupen'),
    path('add_coupen',views.add_coupen_View,name = "add_coupen"),
    path('cancel_status/<int:id>',views.cancel_status_view,name = "cancel_status"),
    path('sales_report/',views.sales_report_view,name = "sales_report"),
    path('export_as_excel',views.export_as_excel_view,name = "export_as_excel")
]