from django.contrib import admin
from django.urls import path,include
from .views import *

urlpatterns = [

    path('', main_page, name="index"),
    path('register/', register, name="register"),
    path('auth/', auth, name="auth"),
    path('logout/', logout, name="logout"),
    path('lk/', lk, name="lk"),
]
