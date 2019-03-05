from django.db import models

# Create your models here.

class Customer(models.Model):
    email = models.EmailField(unique=True, default='test1@test.com')
    first_name = models.CharField(max_length=256, default='test1')
    last_name = models.CharField(max_length=256,default='test')
    tel_number = models.IntegerField(unique=True, default= '0712345678')
