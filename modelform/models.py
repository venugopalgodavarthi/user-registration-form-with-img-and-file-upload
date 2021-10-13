from django.db import models

# Create your models here.

class register(models.Model):
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    email = models.EmailField()
    phone= models.IntegerField()
    age=models.IntegerField()
    list1=[('MALE','Male'),('FEMALE','Female')]
    gender = models.CharField(max_length=10,choices=list1)
    address = models.CharField(max_length=50)