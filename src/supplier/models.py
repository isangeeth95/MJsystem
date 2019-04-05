from django.db import models

class supplier(models.Model):
    sup_items = (
        ('A', 'Stones'),
        ('B', 'Gold'),
        ('C', 'Silver'),
        ('D', 'Colour Stones'),
    )
    first_Name = models.CharField(max_length=100)#first name of the supplier
    last_Name= models.CharField(max_length= 100)#last name of the supplier
    nic = models.CharField(max_length=10)# NIC of the supllier
    address = models.CharField(max_length= 400)# address of the supllier
    phone_No = models.IntegerField(default=0)# phone number
    supplier_item =models.CharField(max_length= 2 , choices= sup_items)# supplier item list
