# Generated by Django 2.1.5 on 2019-03-04 09:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Earrings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cat', models.CharField(max_length=100)),
                ('date', models.DateField()),
                ('description', models.CharField(max_length=500)),
                ('charges', models.IntegerField()),
                ('stones', models.IntegerField()),
                ('weight', models.IntegerField()),
                ('qty', models.IntegerField()),
                ('craft_id', models.IntegerField()),
                ('status', models.CharField(choices=[('AVAILABLE', 'Item ready to be purchased'), ('SOLD', 'Item Sold'), ('RESTOCKING', 'Item restocking in few days')], default='SOLD', max_length=10)),
                ('issues', models.CharField(default='No issues', max_length=100)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Necleces',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cat', models.CharField(max_length=100)),
                ('date', models.DateField()),
                ('description', models.CharField(max_length=500)),
                ('charges', models.IntegerField()),
                ('stones', models.IntegerField()),
                ('weight', models.IntegerField()),
                ('qty', models.IntegerField()),
                ('craft_id', models.IntegerField()),
                ('status', models.CharField(choices=[('AVAILABLE', 'Item ready to be purchased'), ('SOLD', 'Item Sold'), ('RESTOCKING', 'Item restocking in few days')], default='SOLD', max_length=10)),
                ('issues', models.CharField(default='No issues', max_length=100)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Pendants',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cat', models.CharField(max_length=100)),
                ('date', models.DateField()),
                ('description', models.CharField(max_length=500)),
                ('charges', models.IntegerField()),
                ('stones', models.IntegerField()),
                ('weight', models.IntegerField()),
                ('qty', models.IntegerField()),
                ('craft_id', models.IntegerField()),
                ('status', models.CharField(choices=[('AVAILABLE', 'Item ready to be purchased'), ('SOLD', 'Item Sold'), ('RESTOCKING', 'Item restocking in few days')], default='SOLD', max_length=10)),
                ('issues', models.CharField(default='No issues', max_length=100)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Ring',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cat', models.CharField(max_length=100)),
                ('date', models.DateField()),
                ('description', models.CharField(max_length=500)),
                ('charges', models.IntegerField()),
                ('stones', models.IntegerField()),
                ('weight', models.IntegerField()),
                ('qty', models.IntegerField()),
                ('craft_id', models.IntegerField()),
                ('status', models.CharField(choices=[('AVAILABLE', 'Item ready to be purchased'), ('SOLD', 'Item Sold'), ('RESTOCKING', 'Item restocking in few days')], default='SOLD', max_length=10)),
                ('issues', models.CharField(default='No issues', max_length=100)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
