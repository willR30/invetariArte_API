# Generated by Django 4.2.1 on 2023-05-29 15:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('API_core', '0007_rename_simbol_currencytype_symbol_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='full_name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='equipment_category',
            name='description',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='equipment_category',
            name='name',
            field=models.CharField(max_length=50),
        ),
    ]
