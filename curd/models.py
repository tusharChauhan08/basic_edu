from statistics import mode
from turtle import mode

from django.db import models

class Signup(models.Model):
    id = models.AutoField(primary_key= True)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    mobile = models.CharField(max_length=10)
    password = models.CharField(max_length=100)








