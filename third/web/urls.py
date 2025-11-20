from django.urls import path,include
from .views import *
urlpatterns = [
    path("", index, name= 'index'),
    path("auth", auth, name= 'auth'),
    path("register", register, name= 'register'),
    path("home", home, name= 'home'),
    path("logout", logout, name= 'logout'),
]