from django.db import models

# Create your models here.
class Product(models.Model):
    name=models.CharField(max_length=200)
    price=models.CharField(max_length=100)
    color=models.CharField(max_length=50)
    quantity=models.IntegerField()
    description=models.TextField()


def __str__(self):
    return self.name

class Student(models.Model):
    fullname=models.CharField(max_length=200)
    email=models.EmailField(max_length=200)
    password=models.CharField(max_length=200)

