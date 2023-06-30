from rest_framework import serializers
from .models import Products, Equipment, Equipment_Category, Category, Bill, Bill_state, Sale, BillItems, Month, Year, TypeCustomer, Customer, PaymentType, CurrencyType, productStock
from drf_writable_nested.serializers import WritableNestedModelSerializer

class EquipmentCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model=Equipment_Category
        #campos que van a ser consultados que ya tiene las tablas
        fields=('id','name','description')
        read_only_fields=('id',)

class EquipmentSerializer(serializers.ModelSerializer):
    id_equipment_category = serializers.SlugRelatedField(
        queryset = Equipment_Category.objects.all(), slug_field="name"
    )
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

class CurrencyTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model=CurrencyType
        fields=('id','currency')
        read_only_fields=('id',)


class ProductSerializer(serializers.ModelSerializer):
    #category =serializers.CharField(source="category.name", read_only=True)
    category = serializers.SlugRelatedField(
        queryset = Category.objects.all(), slug_field="name"
    )

    currency = serializers.SlugRelatedField(
        queryset = CurrencyType.objects.all(), slug_field="currency"
    )

    class Meta:
        model=Products
        #campos que van a ser consultados que ya tiene las tablas
        fields=('id','name','description','cost','price', 'currency', 'category')
        read_only_fields=('id',)

class productStockSerializer(serializers.ModelSerializer):

    productName = serializers.SlugRelatedField(
        queryset = Products.objects.all(), slug_field="name"
    )

    class Meta:
        model= productStock
        fields=('id','productName','stock')
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

    customer_Type = serializers.SlugRelatedField(
        queryset = TypeCustomer.objects.all(), slug_field="customerType"
    )
    class Meta:
        model=Customer
        fields=('id','full_name','customer_Type')
        read_only_fields=('id',)

class PaymentTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model=PaymentType
        fields=('id','payment_type')
        read_only_fields=('id',)

class SaleSerializer(serializers.ModelSerializer):

    category = serializers.SlugRelatedField(
        queryset = Category.objects.all(), slug_field="name"
    )

    productName = serializers.SlugRelatedField(
         queryset = Products.objects.all(), slug_field="name"
    )
    
    class Meta:
        model=Sale
        #campos que van a ser consultados que ya tiene las tablas
        fields=('id','productName', 'category','price', 'amount_products','total_sale')
        read_only_fields=('id',)

class BillSerializer(WritableNestedModelSerializer):

    id_month = serializers.SlugRelatedField(
        queryset = Month.objects.all(), slug_field="name"
    )

    id_year = serializers.SlugRelatedField(
        queryset = Year.objects.all(), slug_field="name"
    )

    bill_state = serializers.SlugRelatedField(
        queryset = Bill_state.objects.all(), slug_field="name"
    )
    
    currency_type = serializers.SlugRelatedField(
        queryset = CurrencyType.objects.all(), slug_field="currency"
    )

    payment_type = serializers.SlugRelatedField(
        queryset = PaymentType.objects.all(), slug_field="payment_type"
    )

    customer_type = serializers.SlugRelatedField(
        queryset = TypeCustomer.objects.all(), slug_field="customerType"
    )

    billItems= SaleSerializer(many=True)
    
    class Meta:
        model=Bill
        #campos que van a ser consultados que ya tiene las tablas
        fields=('id', 'billNumber','customer_name', 'customer_type', 'phoneNumber', 'sub_total','iva','total','currency_type','payment_type', 'id_month', 'id_year', 'created_at', 'bill_state', 'billItems')
        read_only_fields=('id',)


class BillItemsSerializer(WritableNestedModelSerializer):

    billItems= SaleSerializer(many=True)

    class Meta:
        model= BillItems
        fields=('id', 'billNumber', 'billItems')
        read_only_fields=('id',)

    """ def create(self, validated_data):
        billItems_data = validated_data.pop('billItems')
        sale = Sale.objects.create(**validated_data)

        for item in billItems_data:
            Sale.objects.create(sale=sale, **item)
            
        return sale """