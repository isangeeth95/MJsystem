# Generated by Django 2.0.6 on 2019-05-20 11:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('craftsmen', '0002_auto_20190408_1456'),
    ]

    operations = [
        migrations.CreateModel(
            name='requestedJewelry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('jewelry', models.CharField(choices=[('Earings', 'Earings'), ('Necklace', 'Necklace'), ('Ring', 'Ring'), ('Pendent', 'Pendent')], max_length=100)),
                ('amountGold', models.CharField(max_length=100)),
                ('noOfStone', models.PositiveIntegerField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='jewelry_requested_image/')),
                ('description', models.TextField()),
            ],
        ),
    ]
