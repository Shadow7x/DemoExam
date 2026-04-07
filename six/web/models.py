from django.db import models

# Create your models here.

class users(models.Model):
    name = models.CharField( max_length=255)
    email = models.CharField( max_length=255)
    password = models.CharField( max_length=255)
    create_at = models.DateField(auto_now_add=True)
    update_at = models.DateField(auto_now=True)

class orders(models.Model):
    user_id = models.ForeignKey(users, on_delete=models.CASCADE)
    name_order = models.CharField( max_length=255)
    count_order = models.CharField( max_length=255)
    phone_order = models.CharField( max_length=255)
    address_order = models.CharField( max_length=255)
    create_at = models.DateField(auto_now_add=True)
    update_at = models.DateField( auto_now=True)
    