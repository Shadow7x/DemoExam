from django.db import models

# Create your models here.


class User(models.Model):
    role = models.CharField(max_length=40)
    surname = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    patronymic = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=50)

    def __str__(self) -> str:
        return f"{self.surname} {self.name} {self.patronymic}"
class OrderLocation(models.Model):
    num = models.CharField(max_length=50)
    address =models.CharField(max_length=150)
    
class Product(models.Model):
    article = models.CharField(max_length=10)
    name = models.CharField(max_length=50)
    counter = models.CharField(max_length=10)
    price = models.IntegerField()
    seller = models.CharField(max_length=30)
    creator = models.CharField(max_length=20)
    type = models.CharField(max_length=30)
    discount = models.IntegerField()
    count = models.IntegerField()
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to="images", blank=True, null=True)
    
    def __str__(self) -> str:
        return self.article

class Order(models.Model):
    num = models.IntegerField()
    article = models.TextField()
    dateCreate = models.DateField()
    dateDelivery = models.DateField( auto_now=False, auto_now_add=False)
    location = models.ForeignKey(OrderLocation, on_delete=models.CASCADE)
    client = models.ForeignKey(User, on_delete=models.CASCADE)
    code = models.IntegerField()
    status = models.CharField(max_length=15)

class NewOrder(models.Model):
    article = models.ForeignKey(Product, on_delete=models.CASCADE)
    status = models.CharField(max_length=15)
    location = models.ForeignKey(OrderLocation, on_delete=models.CASCADE)
    date = models.DateField()
    dateDelivery = models.DateField( auto_now=False, auto_now_add=False)