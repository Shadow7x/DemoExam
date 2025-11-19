from django.db import models


# Create your models here.

class orders(models.Model):
    user_id = models.ForeignKey("users", on_delete=models.CASCADE)
    name_order = models.CharField( max_length=255)
    count_order = models.CharField( max_length=255)
    phone_order = models.CharField( max_length=255)
    address_order = models.CharField( max_length=255)
    created_at =models.DateTimeField( auto_now=True, auto_now_add=False)
    updated_at =models.DateTimeField( auto_now_add=True)
    
class users(models.Model):
    name = models.CharField( max_length=255)
    email = models.CharField( max_length=255)
    password = models.CharField( max_length=255)
    created_at =models.DateTimeField( auto_now=True, auto_now_add=False)
    updated_at =models.DateTimeField( auto_now_add=True)