# Generated by Django 2.1.7 on 2019-04-06 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_delete_customer'),
    ]

    operations = [
        migrations.AddField(
            model_name='online_customer',
            name='profile_pic',
            field=models.ImageField(null=True, upload_to='customer_image/'),
        ),
    ]
