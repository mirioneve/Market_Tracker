"""Defines URL pattern for marketapp."""

from django.urls import path
from . import views

app_name = 'marketapp'

urlpatterns = [
    path('', views.index, name='index'),
    
    path('dashboard/', views.dashboard, name='dashboard'),

    path('products/', views.products, name='products'),
]