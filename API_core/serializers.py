from rest_framework import serializers
from .models import Products

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model=Products
        #campos que van a ser consultados que ya tiene las tablas
        fields=('id','name','description','stock','cost','price')
        read_only_fields=('id',)