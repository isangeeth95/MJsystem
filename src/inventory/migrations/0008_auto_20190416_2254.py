# Generated by Django 2.1.7 on 2019-04-16 17:24

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('supplier', '0002_supplier_phone_no'),
        ('inventory', '0007_auto_20190416_2202'),
    ]

    operations = [
        migrations.AddField(
            model_name='stone',
            name='amount',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='stone',
            name='date',
            field=models.DateField(blank=True, default=datetime.datetime.now),
        ),
        migrations.AddField(
            model_name='stone',
            name='quantity_Details',
            field=models.CharField(blank=True, max_length=500),
        ),
        migrations.AddField(
            model_name='stone',
            name='supplier',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='supplier.supplier'),
        ),
    ]
