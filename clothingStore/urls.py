from xml.etree.ElementInclude import include
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path ('login', views.loginUser, name='login'),
    path ('logout', views.logoutUser, name='logout'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('checkout', views.checkout, name="checkout"),
    path('confirmorder', views.confirmorder, name="confirmorder"),
    path('updateItem', views.updateItem, name="updateItem"),
    path('processOrder', views.processOrder, name="processOrder"),
]