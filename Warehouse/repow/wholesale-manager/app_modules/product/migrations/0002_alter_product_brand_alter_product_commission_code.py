# Generated by Django 4.1.7 on 2023-06-20 06:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='brand',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_brand', to='product.brand'),
        ),
        migrations.AlterField(
            model_name='product',
            name='commission_code',
            field=models.FloatField(choices=[(0.0, '0.00%'), (0.01, '0.01%'), (1.0, '1.00%')], verbose_name='Commission Code'),
        ),
    ]
