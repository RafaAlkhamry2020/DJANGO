# Generated by Django 3.0.7 on 2020-07-25 05:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_product_image'),
        ('carts', '0004_auto_20200718_1929'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='items',
            field=models.ManyToManyField(to='products.Product'),
        ),
    ]
