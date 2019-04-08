# Generated by Django 2.1.5 on 2019-04-06 12:09

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0005_auto_20190316_1159'),
    ]

    operations = [
        migrations.CreateModel(
            name='gold',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.IntegerField()),
                ('supplier', models.CharField(max_length=500)),
                ('txt', models.DateField(default=datetime.datetime.now)),
                ('R', models.CharField(max_length=500)),
                ('Is', models.CharField(max_length=500)),
                ('gBal', models.CharField(max_length=500)),
                ('cp', models.FloatField()),
                ('cd', models.FloatField()),
                ('bal', models.FloatField()),
                ('gwa', models.CharField(max_length=500)),
            ],
        ),
    ]