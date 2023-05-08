from rest_framework import viewsets, permissions
from .models import Products
from .serializers import ProductSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response

class ProductsViewSet(viewsets.ModelViewSet):
    # Consultamos todos los productos
    queryset = Products.objects.all()
    # Indicamos los permisos, cualquier app cliente puede consultar datos pero luego se puede cambiar
    permission_classes = [permissions.AllowAny]
    serializer_class = ProductSerializer
