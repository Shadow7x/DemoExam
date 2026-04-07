from django.shortcuts import render,redirect
from .models import *


# Create your views here.

user = None

def main_page(request):
    return render(request, "web/index.html", {"user": user})

def register(request):
    if request.method =="POST":
        data = request.POST
        name = data.get("name")
        email = data.get("email")
        password = data.get("password")
        password2 = data.get("password2")
        if password != password2 :
            return render(request, "web/register.html", {"user": user, "error":"Пороли не совпадают"})
        if users.objects.filter(email = email).exists():
            return render(request, "web/register.html", {"user": user, "error":"Пользователь с такой почтой уже существует"})
        new_user = users.objects.create(name = name, email = email, password = password)
        return redirect("auth")
    else:
        return render(request, "web/register.html", {"user": user})

def auth(request):
    global user
    if request.method =="POST":
        data = request.POST
        password = data.get("password")
        email = data.get("email")
        if not users.objects.filter(email=email,password=password).exists():
            return render(request, "web/auth.html", {"user": user, "error":"Такого пользователя не существует"})
        user = users.objects.filter(email=email,password=password).first()
        return redirect("lk")
    else:
        return render(request, "web/auth.html", {"user": user})

def logout(request):
    global user
    user = None
    return redirect("/")

def lk(request):
    if request.method =="POST":
        data = request.POST
        name = data.get("name")
        count = data.get("count")
        phone = data.get("phone")
        address = data.get("address")
        orders.objects.create(name_order = name,count_order = count,phone_order=phone, address_order= address, user_id=user )
    
    if user is None:
        return redirect("/")
    
    order = orders.objects.filter(user_id  = user)
    return render(request, "web/lk.html", {"user": user, "order": order})