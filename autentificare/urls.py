from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.autentificare, name='autentificare'),
    path('loginpage/', views.loginpage, name='loginpage'),
    path('logoutuser/', views.logoutuser, name='logoutuser'),


]
