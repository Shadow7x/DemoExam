from django.shortcuts import render,redirect
from .models import *


# Create your views here.

user = None

def index(request):
    global user
    return render(request, "web/main.html", {"users": user})

def register(request):
    global user
    if request.method =="POST":
        data = request.POST
        if data["password"] == data["password2"]:
            if users.objects.filter(email=data['email']).exists():
                return render(request, "web/register.html", {"error" : "Такой пользователь уже существует","users": user})
            users.objects.create(name=data["name"], email = data["email"], password = data["password"])
            redirect('auth')
        else:
            return render(request, "web/register.html", {"error" : "Пороли не совпадают","users": user})
    return render(request, "web/register.html", {"users": user})

def auth(request):
    global user
    if request.method =="POST":
        data = request.POST
        if users.objects.filter(email=data["email"], password = data["password"]).exists():
            user =  users.objects.filter(email=data["email"], password = data["password"]).first()
            return redirect("home")
        else:
            return render(request, "web/auth.html", {"error" : "Такого пользователя не существует","users": user})
    return render(request, "web/auth.html", {"users": user})


def home(request):
    global user
    order = orders.objects.filter(user_id=user)
    print(orders)
    return render(request, "web/home.html", {"users": user, 'orders':order})

def logout(request):
    global user
    user = None
    return redirect("/")

def create(request):
    global user
    if user:
        if request.method =="POST":
            data = request.POST
            orders.objects.create(user_id = user, name_order=data["name"], count_order=data["count"], phone_order=data["phone"], address_order=data["address"])
            return redirect("home")
        return render(request, "web/create.html", {"users": user})
    else:
        return redirect("/")