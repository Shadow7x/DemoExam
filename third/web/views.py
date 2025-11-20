from django.shortcuts import render, redirect
from .models import *


# Create your views here.

user=None

def index(request):
    global user
    return render(request, "web/index.html", {'user':user})

def register(request):
    global user
    if request.method =="POST":
        data = request.POST
        name = data["name"]
        email = data["email"]
        password = data["password"]
        password2 = data["password2"]
        if len(password.replace(" ", "")) <8:
            return render(request, "web/register.html", {'user':user,'error':"Пороль должен быть больше 8 символов"})
        if password !=password2:
            return render(request, "web/register.html", {'user':user,'error':"Пороли не совпадают"})
        if users.objects.filter(email = email).exists():
            return render(request, "web/register.html", {'user':user,'error':"Такой пользователь уже существует"})
        users.objects.create(name = name, email = email, password = password)
        return redirect('auth')
        
    return render(request, "web/register.html", {'user':user})

def auth(request):
    global user
    if request.method =="POST":
        data = request.POST
        email = data["email"]
        password = data["password"]
        if not users.objects.filter(email = email, password = password).exists():
            return render(request, "web/auth.html", {'user':user, 'error': "Такого пользователя не существует"})
        user = users.objects.filter(email = email, password = password).first()
        return redirect("home")
    
    return render(request, "web/auth.html", {'user':user})


def logout(request):
    global user
    user = None
    return redirect("/")
    
def home(request):
    global user
    if user:
        if request.method =="POST":
            data = request.POST
            name = data["name"]
            count = data["count"]
            phone = data["phone"]
            address = data['address']
            orders.objects.create(user_id = user, name_order = name, count_order = count, phone_order = phone, address_order = address)
        order = orders.objects.filter(user_id = user)
        
        return render(request, "web/home.html", {'user':user,"orders":order})
    return redirect("/")