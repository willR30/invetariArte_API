from rest_framework import serializers
from .models import Products, Equipment, Equipment_Category, Category, Bill, Bill_state, Sale, Month, Year, TypeCustomer, Customer

class EquipmentCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model=Equipment_Category
        #campos que van a ser consultados que ya tiene las tablas
        fields=('id','name','description')
        read_only_fields=('id',)

class EquipmentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Equipment
        #campos que van a ser consultados que ya tiene las tablas
        fields=('id','name','id_equipment_category')
        read_only_fields=('id',)

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model=Category
        #campos que van a ser consultados que ya tiene las tablas
        fields=('id','name','description')
        read_only_fields=('id',)


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model=Products
        #campos que van a ser consultados que ya tiene las tablas
        fields=('id','name','description','stock','cost','price','id_category')
        read_only_fields=('id',)

class BillStateSerializer(serializers.ModelSerializer):
    class Meta:
        model=Bill_state
        #campos que van a ser consultados que ya tiene las tablas
        fields=('id','name')
        read_only_fields=('id',)

class MonthSerializer(serializers.ModelSerializer):
    class Meta:
        model=Month
        #campos que van a ser consultados que ya tiene las tablas
        fields=('id','name')
        read_only_fields=('id',)

class YearSerializer(serializers.ModelSerializer):
    class Meta:
        model=Year
        #campos que van a ser consultados que ya tiene las tablas
        fields=('id','name')
        read_only_fields=('id',)

class TypeCustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model=TypeCustomer
        fields=('id','customerType')
        read_only_fields=('id',)

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model=Customer
        fields=('id','full_name','type')
        read_only_fields=('id',)

class BillSerializer(serializers.ModelSerializer):
    class Meta:
        model=Bill
        #campos que van a ser consultados que ya tiene las tablas
        fields=('id','date','customer_name','sub_total','iva','total', 'id_month', 'id_year', 'id_bill_state')
        read_only_fields=('id',)

class SaleSerializer(serializers.ModelSerializer):
    class Meta:
        model=Sale
        #campos que van a ser consultados que ya tiene las tablas
        fields=('id','id_bill','id_products','amount_products','price_at_moment','total_sale')
        read_only_fields=('id',)
