from rest_framework import viewsets, permissions
from .models import Products, Equipment, Equipment_Category, Category, Bill, Bill_state, Sale, Month, Year
from .serializers import ProductSerializer, EquipmentSerializer,EquipmentCategorySerializer, CategorySerializer, BillSerializer,BillStateSerializer,YearSerializer, MonthSerializer, SaleSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response



class EquipmentCategoryViewSet(viewsets.ModelViewSet):
    # Consultamos todos los productos
    queryset = Equipment_Category.objects.all()
    # Indicamos los permisos, cualquier app cliente puede consultar datos pero luego se puede cambiar
    permission_classes = [permissions.AllowAny]
    serializer_class = EquipmentCategorySerializer

class EquipmentViewSet(viewsets.ModelViewSet):
    queryset = Equipment.objects.all()
    # Indicamos los permisos, cualquier app cliente puede consultar datos pero luego se puede cambiar
    permission_classes = [permissions.AllowAny]
    serializer_class = EquipmentSerializer

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    # Indicamos los permisos, cualquier app cliente puede consultar datos pero luego se puede cambiar
    permission_classes = [permissions.AllowAny]
    serializer_class = CategorySerializer

class ProductsViewSet(viewsets.ModelViewSet):
    # Consultamos todos los productos
    queryset = Products.objects.all()
    # Indicamos los permisos, cualquier app cliente puede consultar datos pero luego se puede cambiar
    permission_classes = [permissions.AllowAny]
    serializer_class = ProductSerializer

class BillStateViewSet(viewsets.ModelViewSet):
    queryset = Bill_state.objects.all()
    # Indicamos los permisos, cualquier app cliente puede consultar datos pero luego se puede cambiar
    permission_classes = [permissions.AllowAny]
    serializer_class = BillStateSerializer

class MonthViewSet(viewsets.ModelViewSet):
    queryset = Month.objects.all()
    # Indicamos los permisos, cualquier app cliente puede consultar datos pero luego se puede cambiar
    permission_classes = [permissions.AllowAny]
    serializer_class = MonthSerializer

class YearViewSet(viewsets.ModelViewSet):
    queryset = Year.objects.all()
    # Indicamos los permisos, cualquier app cliente puede consultar datos pero luego se puede cambiar
    permission_classes = [permissions.AllowAny]
    serializer_class = YearSerializer

class BillViewSet(viewsets.ModelViewSet):
    queryset = Bill.objects.all()
    # Indicamos los permisos, cualquier app cliente puede consultar datos pero luego se puede cambiar
    permission_classes = [permissions.AllowAny]
    serializer_class = BillSerializer

class SaleViewSet(viewsets.ModelViewSet):
    queryset = Sale.objects.all()
    # Indicamos los permisos, cualquier app cliente puede consultar datos pero luego se puede cambiar
    permission_classes = [permissions.AllowAny]
    serializer_class = SaleSerializer
