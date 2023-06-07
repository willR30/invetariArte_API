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
    name=models.CharField(max_length=30)
    description=models.CharField(max_length=200)

    def __str__(self):
        return  self.name

class Equipment(models.Model):
    """
        Los equipos  para TRABAJAR INTERNAMENTE A FIN DE REPARAR OTROS EQUIPOS  que pertenecen a una categoría en específico (que ya fue registrada)
        ejemplo:
            Categoria: Soldadores
            producto : Cautin Industrial
    """
    name=models.CharField(max_length=30)
    id_equipment_category=models.ForeignKey(Equipment_Category,on_delete=models.CASCADE)#establecemos la relacion

class Category(models.Model):
    """
        Categoria de los productos a vender al publico
        ejemplo: Premiun, Seguridad, Telefono, Computadoras, Impresoras, Solo para empresas , etc...
    """
    name=models.CharField(max_length=30)
    description=models.CharField(max_length=200)

    def __str__(self) :
        return self.name

class Products(models.Model):
    """
        Productos que se venden al público
        ejemplo:
            Categoria: Solo empresas
            Producto: Impresora industrial xl123
    """
    #the Id is for default
    name=models.CharField(max_length=30)
    description=models.CharField(max_length=200)
    stock=models.IntegerField()
    cost=models.FloatField()
    price=models.FloatField()
    #category=models.ForeignKey(Category).name
    category=models.ForeignKey(Category,on_delete=models.CASCADE)#Cada producto pertence a una categoria

    def __str__(self) :
        return self.name

class Bill_state(models.Model):
    """
        Una factura puede tener un estado
        Ejemplo: Activa y/o Anulada
    """
    name=models.CharField(max_length=10)

    def __str__(self) :
        return self.name

class Month(models.Model):
    name=models.CharField(max_length=30)

    def __str__(self) :
        return self.name

class Year(models.Model):
    name=models.CharField(max_length=30)
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
    customerType=models.CharField(max_length=50)

    def __str__(self) :
        return self.customerType

class Customer(models.Model):
    """
        El cliente como tal que previamente fue registrado
    """
    full_name=models.CharField(max_length=10)
    type=models.ForeignKey(TypeCustomer, on_delete=models.CASCADE)

    def __str__(self) :
        return self.full_name

class CurrencyType(models.Model):
    """
        Ej: C$-Cordobas, $-Dolar etc..
    """
    currency=models.CharField(max_length=20)
    symbol=models.CharField(max_length=5)

    def __str__(self) -> str:
        return f'{self.symbol} {self.currency}'

class PaymentType(models.Model):
    """
        Tipos de pago:
            -Efectivo
            -Transferencia
    """
    payment_type=models.CharField(max_length=20)

    def __str__(self) :
        return self.payment_type

class Bill(models.Model):
    """
        La factura asociada a un cliente, esta (la factura) tiene un estado, se cancelo con un tipo de pago y fue facturada con una moneda en específico
    """
    date=models.DateField()
    customer_name=models.ForeignKey(Customer,on_delete=models.CASCADE)#La factura pertenece a un cliente previamente registrado
    sub_total=models.FloatField()
    iva=models.FloatField()
    total=models.FloatField()
    id_month=models.ForeignKey(Month, on_delete=models.CASCADE)
    id_year=models.ForeignKey(Year, on_delete=models.CASCADE)
    id_bill_state=models.ForeignKey(Bill_state,on_delete=models.CASCADE)
    id_currency_type=models.ForeignKey(CurrencyType, on_delete=models.CASCADE, null=True)
    id_payment_type=models.ForeignKey(PaymentType, on_delete=models.CASCADE,null=True)

class Sale(models.Model):
    """
        Cada venta esta asociada a una factura y un producto (el que fue vendido)
    """
    id_bill=models.ForeignKey(Bill, on_delete=models.CASCADE)
    id_products=models.ForeignKey(Products,on_delete=models.CASCADE)
    amount_products=models.IntegerField()
    price_at_moment=models.FloatField()
    total_sale=models.FloatField()