from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
   path('', views.index),
   path('products/', views.Products),
   path('customer/<str:c_id>/', views.Customer),
]
