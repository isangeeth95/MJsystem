# Generated by Django 2.1.5 on 2019-04-08 09:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('craftsmen', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='craftsmen',
            name='craftsmen_Item',
            field=models.CharField(choices=[('Earings', 'Earings'), ('Necklace', 'Necklace'), ('Ring', 'Ring'), ('Pendent', 'Pendent')], max_length=100),
        ),
    ]