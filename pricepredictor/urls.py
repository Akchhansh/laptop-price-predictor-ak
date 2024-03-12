from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('', views.forms, name='forms'),
    path('predict_price/', views.predict_price, name='predict_price'),
]