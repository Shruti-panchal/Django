from django.contrib import admin
from django.urls import path
from . import views

app_name = 'food'
urlpatterns = [
    path('index/', views.index, name='index'),
    path('', views.home, name='home'),
    path ('item/', views.item, name='item'),
    path ('<int:item_id>/', views.detail, name='detail'),
]