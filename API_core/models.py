from django.db import models

# Create your models here.

class Products(models.Model):
    #the Id is for default
    name=models.CharField(max_length=30)
    description=models.CharField(max_length=30)
    stock=models.IntegerField()
    cost=models.FloatField()
    price=models.FloatField()
    #Products category pendiente
