# Generated by Django 4.2.1 on 2023-05-21 02:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('API_core', '0005_currencytype_paymenttype_alter_bill_customer_name_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bill',
            old_name='id_paymen_type',
            new_name='id_payment_type',
        ),
    ]