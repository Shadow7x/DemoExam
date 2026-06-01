from django.db import models

# Create your models here.

class User(models.Model):
    role = models.CharField( max_length=50)
    surname = models.CharField( max_length=50)
    name = models.CharField( max_length=50)
    patronymic = models.CharField( max_length=50)
    login = models.CharField( max_length=50)
    password = models.CharField( max_length=50)
    
    def __str__(self) -> str:
        return f"{self.surname} {self.name} {self.patronymic}"

class Hall(models.Model):
    name = models.CharField( max_length=50)
    rows = models.PositiveSmallIntegerField()
    columns = models.PositiveSmallIntegerField()
    

class Cinema(models.Model):
    code = models.CharField( max_length=50)
    name = models.CharField( max_length=50)
    price = models.PositiveIntegerField()
    hall = models.ForeignKey(Hall, on_delete=models.CASCADE)
    producer = models.CharField( max_length=50)
    genre = models.CharField( max_length=50)
    discount = models.PositiveSmallIntegerField()
    Description = models.TextField()
    image = models.ImageField(upload_to='Images/', blank=True, null=True)

class Ticket(models.Model):
    cinema = models.ForeignKey(Cinema, on_delete=models.CASCADE)
    row = models.PositiveSmallIntegerField()
    column = models.PositiveSmallIntegerField()
    booking = models.ForeignKey("Booking", on_delete=models.CASCADE)
    

class Booking(models.Model):
    tickets = models.ManyToManyField(through=Ticket, to = Cinema)
    date = models.DateField()
    date_seance = models.DateField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    code = models.CharField(max_length=50)
    status = models.CharField(max_length=50)