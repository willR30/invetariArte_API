from django.db import models


# Create your models here.
class Equipment_Category(models.Model):
    name=models.CharField(max_length=30)
    description=models.CharField(max_length=200)

class Equipment(models.Model):
    name=models.CharField(max_length=30)
    id_equipment_category=models.ForeignKey(Equipment_Category,on_delete=models.CASCADE)#establecemos la relacion

class Category(models.Model):
    name=models.CharField(max_length=30)
    description=models.CharField(max_length=200)

class Products(models.Model):
    #the Id is for default
    name=models.CharField(max_length=30)
    description=models.CharField(max_length=200)
    stock=models.IntegerField()
    cost=models.FloatField()
    price=models.FloatField()
    id_category=models.ForeignKey(Category,on_delete=models.CASCADE)#Cada producto pertence a una categoria

class Bill_state(models.Model):
    name=models.CharField(max_length=10)

class Month(models.Model):
    name=models.CharField(max_length=30)

class Year(models.Model):
    name=models.CharField(max_length=30)


class TypeCustomer(models.Model):
    """
        we can have many customer types: Particular Customer, busisnes
    """
    customerType=models.CharField(max_length=50)

class Customer(models.Model):
    full_name=models.CharField(max_length=10)
    type=models.ForeignKey(TypeCustomer, on_delete=models.CASCADE)


class Bill(models.Model):
    date=models.DateField()
    customer_name=models.CharField(max_length=50)
    sub_total=models.FloatField()
    iva=models.FloatField()
    total=models.FloatField()
    id_month=models.ForeignKey(Month, on_delete=models.CASCADE)
    id_year=models.ForeignKey(Year, on_delete=models.CASCADE)
    id_bill_state=models.ForeignKey(Bill_state,on_delete=models.CASCADE)

class Sale(models.Model):
    id_bill=models.ForeignKey(Bill, on_delete=models.CASCADE)
    id_products=models.ForeignKey(Products,on_delete=models.CASCADE)
    amount_products=models.IntegerField()
    price_at_moment=models.FloatField()
    total_sale=models.FloatField()
