# Generated by Django 2.1.7 on 2019-03-11 13:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DeliveryInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Order_No', models.CharField(max_length=6)),
                ('UserName', models.CharField(max_length=100)),
                ('Receiver_Name', models.CharField(max_length=200)),
                ('Receiver_Add', models.CharField(max_length=300)),
                ('Telephone_No', models.IntegerField()),
                ('Order_date', models.DateTimeField(auto_now=True)),
                ('Deliver_date', models.DateTimeField()),
            ],
        ),
    ]