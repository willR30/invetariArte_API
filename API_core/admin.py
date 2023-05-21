from django.contrib import admin
from .models import Products, Equipment, Equipment_Category, Category, Bill, Bill_state, Sale, Month, Year, TypeCustomer, Customer, PaymentType, CurrencyType
# Register your models here.

admin.site.register(Products)
admin.site.register(Equipment_Category)
admin.site.register(Equipment)
admin.site.register(Category)
admin.site.register(Bill)
admin.site.register(Bill_state)
admin.site.register(Sale)
admin.site.register(Month)
admin.site.register(Year)
admin.site.register(TypeCustomer)
admin.site.register(Customer)
admin.site.register(PaymentType)
admin.site.register(CurrencyType)
