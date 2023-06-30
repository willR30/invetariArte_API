from datetime import timezone
from django.db import models


# Create your models here.
class Equipment_Category(models.Model):
    """
        Esta tabla es para las CATEGORIAS de el material que se utilizar PARA REPARAR  diferentes equipos
        ejemplo:
            -Desarmadores
            -Soldarores
            -Productos quimicos 
            -etc ...
    """
    name=models.CharField(max_length=500)
    description=models.CharField(max_length=500)

    def __str__(self):
        return  self.name

class Equipment(models.Model):
    """
        Los equipos  para TRABAJAR INTERNAMENTE A FIN DE REPARAR OTROS EQUIPOS  que pertenecen a una categoría en específico (que ya fue registrada)
        ejemplo:
            Categoria: Soldadores
            producto : Cautin Industrial
    """
    name=models.CharField(max_length=500)
    id_equipment_category=models.ForeignKey(Equipment_Category,on_delete=models.CASCADE)#establecemos la relacion

class Category(models.Model):
    """
        Categoria de los productos a vender al publico
        ejemplo: Premiun, Seguridad, Telefono, Computadoras, Impresoras, Solo para empresas , etc...
    """
    name=models.CharField(max_length=500)
    description=models.CharField(max_length=500)

    def __str__(self) :
        return self.name
    
class CurrencyType(models.Model):
    """
        Ej: C$-Cordobas, $-Dolar etc..
    """
    currency=models.CharField(max_length=50)

    def __str__(self):
        return self.currency

class Products(models.Model):
    """
        Productos que se venden al público
        ejemplo:
            Categoria: Solo empresas
            Producto: Impresora industrial xl123
    """
    #the Id is for default
    name=models.CharField(max_length=500)
    description=models.CharField(max_length=500)
    #stock=models.IntegerField(null=True)
    cost=models.FloatField()
    price=models.FloatField()
    currency=models.ForeignKey(CurrencyType, on_delete=models.CASCADE, null=True)
    category=models.ForeignKey(Category,on_delete=models.CASCADE)#Cada producto pertence a una categoria

    def __str__(self) :
        return self.name
    
class productStock(models.Model):
    productName=models.ForeignKey(
        Products, 
        on_delete=models.CASCADE
    )

    """  productStock=models.ForeignKey(
        Products, 
        related_name="stock",
        null=True,
        on_delete=models.CASCADE
    ) """
    stock=models.IntegerField(null=True)
    #quantity= models.ForeignKey(Products, on_delete=models.CASCADE)

class Bill_state(models.Model):
    """
        Una factura puede tener un estado
        Ejemplo: Activa y/o Anulada
    """
    name=models.CharField(max_length=200) # puede ser Activada, desactivada

    def __str__(self) :
        return self.name

class Month(models.Model):
    name=models.CharField(max_length=100)

    def __str__(self) :
        return self.name

class Year(models.Model):
    name=models.CharField(max_length=100)
    def __str__(self) :
        return self.name


class TypeCustomer(models.Model):
    """
        Se pueden manejar diferentes tipos de clientes
        ejemplo:
            -Persona Natural
            -Empresa
            -O.N.G.
            -Etc
    """
    customerType=models.CharField(max_length=500)

    def __str__(self) :
        return self.customerType

class Customer(models.Model):
    """
        El cliente como tal que previamente fue registrado
    """
    full_name=models.CharField(max_length=500)
    customer_Type=models.ForeignKey(TypeCustomer, on_delete=models.CASCADE)

    def __str__(self) :
        return self.full_name

class PaymentType(models.Model):
    """
        Tipos de pago:
            -Efectivo
            -Transferencia
    """
    payment_type=models.CharField(max_length=100)

    def __str__(self) :
        return self.payment_type

class Sale(models.Model):
    """
        Cada venta esta asociada a una factura y un producto (el que fue vendido)
        Este es el detalle de la facura, los productos comprados con su cantidad
    """
    #billNumber=models.ForeignKey(Bill, related_name='bill',on_delete=models.CASCADE)
    #billNumber=models.CharField(max_length=20, null=False, unique=True)
    productName=models.ForeignKey(Products, on_delete=models.CASCADE)
    category=models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    price=models.DecimalField(default=0, max_digits=20, decimal_places=2)
    amount_products=models.CharField(max_length=10, null=False, blank=True)
    total_sale=models.DecimalField(default=0, max_digits=20, decimal_places=2)
    """ price_at_moment=models.DecimalField(default=0, max_digits=20, decimal_places=2)
    amount_products=models.PositiveBigIntegerField()
    total_sale=models.DecimalField(default=0, max_digits=20, decimal_places=2) """
    
class Bill(models.Model):
    """
        La factura asociada a un cliente, esta (la factura) tiene un estado, se cancelo con un tipo de pago y fue facturada con una moneda en específico
    """
    billNumber=models.CharField(max_length=20, null=False, unique=True)
    customer_name=models.CharField(max_length=500) #La factura pertenece a un cliente previamente registrado
    customer_type=models.ForeignKey(TypeCustomer, on_delete=models.CASCADE)
    phoneNumber = models.CharField(max_length=9, null=False, blank=True)
    sub_total=models.DecimalField(max_digits=20, decimal_places=2)
    iva=models.DecimalField(max_digits=20, decimal_places=2)
    total=models.DecimalField(max_digits=20, decimal_places=2)
    currency_type=models.ForeignKey(CurrencyType, on_delete=models.CASCADE, null=True)
    payment_type=models.ForeignKey(PaymentType, on_delete=models.CASCADE,null=True)
    id_month=models.ForeignKey(Month, on_delete=models.CASCADE)
    id_year=models.ForeignKey(Year, on_delete=models.CASCADE)
    created_at=models.DateField()
    bill_state=models.ForeignKey(Bill_state, on_delete=models.CASCADE)
    billItems=models.ManyToManyField(Sale)

    def __str__(self):
        return self.billNumber
    #bill_items=models.ManyToManyField(Sale)
    #bill_items=models.ManyToManyField(Products, through='Sale')

class BillItems(models.Model):
    billNumber=models.CharField(max_length=20, null=False, unique=True)
    #billNumber=models.ForeignKey(Bill, on_delete=models.CASCADE)
    billItems=models.ManyToManyField(Sale)

    """ def __str__(self) :
        return self.billNumber """
    
""" class DateRangeForms(forms.Form):
    start_date = forms.DateField()
    end_date = forms.DateField() """