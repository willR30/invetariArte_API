from rest_framework import viewsets, permissions
from .models import Products, Equipment, Equipment_Category, Category, Bill, Bill_state, Sale, BillItems,Month, Year, TypeCustomer, Customer, PaymentType, CurrencyType, productStock
from .serializers import ProductSerializer, EquipmentSerializer,EquipmentCategorySerializer, CategorySerializer, BillSerializer, BillItemsSerializer,BillStateSerializer,YearSerializer, MonthSerializer, SaleSerializer, TypeCustomerSerializer, CustomerSerializer, PaymentTypeSerializer, CurrencyTypeSerializer, productStockSerializer
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

class TypeCustomerViewSet(viewsets.ModelViewSet):
    queryset = TypeCustomer.objects.all()
    permission_classes=[permissions.AllowAny]
    serializer_class=TypeCustomerSerializer

class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    permission_classes=[permissions.AllowAny]
    serializer_class=CustomerSerializer

class ProductsViewSet(viewsets.ModelViewSet):
    # Consultamos todos los productos
    queryset = Products.objects.all()
    # Indicamos los permisos, cualquier app cliente puede consultar datos pero luego se puede cambiar
    permission_classes = [permissions.AllowAny]
    serializer_class = ProductSerializer

class productStockViewSet(viewsets.ModelViewSet):
    queryset = productStock.objects.all()
     # Indicamos los permisos, cualquier app cliente puede consultar datos pero luego se puede cambiar
    permission_classes = [permissions.AllowAny]
    serializer_class = productStockSerializer

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

class CurrencyTypeViewSet(viewsets.ModelViewSet):
    queryset=CurrencyType.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = CurrencyTypeSerializer

class PaymentTypeViewSet(viewsets.ModelViewSet):
    queryset=PaymentType.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = PaymentTypeSerializer

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

class BillItemsViewSet(viewsets.ModelViewSet):
    queryset = BillItems.objects.all()
    # Indicamos los permisos, cualquier app cliente puede consultar datos pero luego se puede cambiar
    permission_classes = [permissions.AllowAny]
    serializer_class = BillItemsSerializer

