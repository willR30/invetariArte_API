from django.shortcuts import render

from rest_framework import viewsets

from .models import Products
from .serializers import ProductSerializer

class TotalProductsViewSet(viewsets.ModelViewSet):

    serializer_class = ProductSerializer
    queryset = Products.objects.all()
    total_sales= queryset.count()
