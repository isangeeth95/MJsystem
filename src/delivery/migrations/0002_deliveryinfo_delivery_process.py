# Generated by Django 2.1.7 on 2019-04-09 17:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('delivery', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='deliveryinfo',
            name='Delivery_Process',
            field=models.CharField(choices=[('Request', 'Request'), ('OnProcess', 'Processing'), ('onDelivery', 'on Delivery'), ('Delivered', 'delivered')], default='Request', max_length=100),
        ),
    ]
