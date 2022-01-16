from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.user_signup,name='signup') # cout
]