# Generated by Django 2.1.5 on 2019-03-16 06:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0003_jewelry_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jewelry',
            name='charges',
            field=models.DecimalField(decimal_places=2, max_digits=6),
        ),
        migrations.AlterField(
            model_name='jewelry',
            name='weight',
            field=models.DecimalField(decimal_places=2, max_digits=6),
        ),
    ]
