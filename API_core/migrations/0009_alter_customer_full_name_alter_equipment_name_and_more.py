# Generated by Django 4.2.1 on 2023-06-06 22:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('API_core', '0008_alter_customer_full_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='full_name',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='equipment',
            name='name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='equipment_category',
            name='description',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='products',
            name='description',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='products',
            name='name',
            field=models.CharField(max_length=200),
        ),
    ]
