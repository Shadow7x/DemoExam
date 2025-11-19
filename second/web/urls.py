from django.urls import path
from .views import *


urlpatterns =[
    path("", index),
    path("register", register, name='register'),
    path("auth", auth, name='auth'),
    path("home", home, name='home'),
    path("logout", logout, name='logout'),
    path("create", create, name='create'),
]