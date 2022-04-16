from xml.etree.ElementInclude import include
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    # path('register', views.register, name='register'),
    # path('login', views.Customerlogin, name='login'),
    path ('login', views.loginPage, name='login'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('checkout', views.checkout, name="checkout"),
    path('uploaditem', views.uploaditem, name="uploaditem"),
    path('viewproduct', views.viewproduct, name="viewproduct"),
    path('confirmorder', views.confirmorder, name="confirmorder"),
    path('updateItem', views.updateItem, name="updateItem"),
    path('processOrder', views.processOrder, name="processOrder"),
]