from django.db import models

# Create your models here.


class User(models.Model):
    role = models.CharField( max_length=50)
    surname = models.CharField( max_length=250)
    name = models.CharField( max_length=250)
    patronymic = models.CharField( max_length=250)
    email = models.CharField( max_length=50)
    password = models.CharField( max_length=50)
    
    def __str__(self) -> str:
        return f"{self.surname} {self.name} {self.patronymic}"
    
class Product(models.Model):
    article = models.CharField(max_length=10)
    name = models.CharField(max_length=40)
    counter =models.CharField(max_length=10)
    price = models.IntegerField()
    seller = models.CharField(max_length=30)
    creator = models.CharField(max_length=40)
    type = models.CharField(max_length=30)
    discount = models.IntegerField()
    count = models.IntegerField()
    description = models.TextField()
    image = models.ImageField(upload_to="Product", null=True, blank=True)
    
    def __str__(self) -> str:
        return self.article

class OrderLocation(models.Model):
    num = models.CharField(max_length=30)
    address = models.CharField(max_length=60)

class OrderDetails(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    order = models.ForeignKey("Order", on_delete=models.CASCADE )
    count = models.IntegerField(default=1)

class Order(models.Model):
    num = models.IntegerField()
    orders = models.ManyToManyField(Product, through=OrderDetails)
    date = models.DateField()
    dateDelivery = models.DateField()
    location = models.ForeignKey(OrderLocation, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    code = models.IntegerField()
    status = models.CharField(max_length=30)

