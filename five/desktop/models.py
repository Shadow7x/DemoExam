from django.db import models

# Create your models here.

class Product(models.Model):
    article = models.CharField( max_length=20)
    name = models.CharField( max_length=55)
    price = models.PositiveIntegerField()
    seller = models.CharField( max_length=30)
    creator = models.CharField( max_length=30)
    type = models.CharField( max_length=30)
    discount = models.PositiveIntegerField()
    count = models.PositiveIntegerField()
    description = models.TextField()
    image = models.ImageField(upload_to="./Images", blank=True, null=True)

    def __str__(self) -> str:
        return self.article
    
class User(models.Model):
    role = models.CharField( max_length=50)
    surname = models.CharField( max_length=30)
    name = models.CharField( max_length=30)
    patronymic = models.CharField( max_length=30)
    login = models.CharField( max_length=20)
    password = models.CharField( max_length=20)
    
    def __str__(self) -> str:
        return f"{self.surname} {self.name} {self.patronymic}"

class OrderLocation(models.Model):
    address = models.TextField()

class Order(models.Model):
    num = models.IntegerField()
    date = models.DateField()
    date_delivery =  models.DateField()
    order_location = models.ForeignKey(OrderLocation, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    code = models.IntegerField()
    status = models.CharField( max_length=30)
    cart = models.ManyToManyField(Product, through="OrderDetails")


class OrderDetails(models.Model):
    order =models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    count = models.IntegerField()