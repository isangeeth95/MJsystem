# Generated by Django 2.1.5 on 2019-04-08 09:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='craftsmen',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_Name', models.CharField(max_length=100)),
                ('last_Name', models.CharField(max_length=100)),
                ('nic', models.CharField(max_length=10)),
                ('address', models.CharField(max_length=400)),
                ('phone_No', models.IntegerField(default=0)),
                ('craftsmen_Item', models.CharField(choices=[('Earings', 'Earings'), ('Necklace', 'Necklace'), ('Ring', 'Ring'), ('Pendent', 'Pendent')], max_length=4)),
            ],
        ),
    ]
