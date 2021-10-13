from django.db import models

# Create your models here.

class register(models.Model):
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    email = models.EmailField()
    phone= models.BigIntegerField()
    age=models.IntegerField()
    list1=[('MALE','Male'),('FEMALE','Female')]
    gender = models.CharField(max_length=10,choices=list1)
    address = models.CharField(max_length=50)
    img= models.ImageField(upload_to="images")
    file= models.FileField(upload_to="files")