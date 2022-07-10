from django.contrib import admin
from django.urls import path, include
from profiles import views

urlpatterns = [
    path('', views.add_user),
    path('success/', views.show_profile),
]
