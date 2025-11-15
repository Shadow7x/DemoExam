from django.db import models

# Create your models here.


class User(models.Model):
    role = models.CharField(max_length=30)
    surname= models.CharField(max_length=50)
    name= models.CharField(max_length=50)
    patronymic= models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    
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

class Cart(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    count = models.IntegerField()
    
class Order(models.Model):
    num = models.IntegerField()
    orders = models.ManyToManyField(Cart)
    date = models.DateField()
    dateDelivery = models.DateField()
    location = models.ForeignKey(OrderLocation, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    code = models.IntegerField()
    status = models.CharField(max_length=30)


class NewOrder(models.Model):
    article = models.ForeignKey(Product,  on_delete=models.CASCADE)
    date = models.DateField( auto_now=False, auto_now_add=False)
    dateDelivery = models.DateField( auto_now=False, auto_now_add=False)
    location = models.ForeignKey(OrderLocation, on_delete=models.CASCADE)
    status = models.CharField( max_length=50)