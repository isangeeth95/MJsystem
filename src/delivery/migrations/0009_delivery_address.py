# Generated by Django 2.1.7 on 2019-05-11 16:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('billing', '0001_initial'),
        ('delivery', '0008_auto_20190501_0100'),
    ]

    operations = [
        migrations.CreateModel(
            name='Delivery_Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address_type', models.CharField(choices=[('delivering', 'Delivering')], max_length=120)),
                ('Receiver_Name', models.CharField(max_length=200)),
                ('Receiver_Add', models.CharField(max_length=300)),
                ('District', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='delivery.DeliveryDistance')),
                ('billing_profile', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='billing.BillingProfile')),
            ],
        ),
    ]
