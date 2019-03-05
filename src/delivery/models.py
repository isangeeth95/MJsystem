from django.db import models

# Create your models here.

class DeliveryInfo(models.Model):

    Order_No = models.CharField(max_length=6, blank=False)
    Item_Code = models.CharField(max_length=6,blank=False)
    Description =models.CharField(max_length=100)
    Weight = models.FloatField()
    Receiver_Name = models.CharField(max_length=200)
    Receiver_Add = models.CharField(max_length=300)
    Order_date = models.DateTimeField(auto_now=True)
    Deliver_date = models.DateTimeField()

    def __str__(self):
        return 'Order_No: {0} Item_Code:{1} Description:{2} Weight:{3} Receiver_Name:{4} Receiver_Add:{5}'.format(self.Order_No, self.Item_Code, self.Description, self.Weight, self.Receiver_Name, self.Receiver_Add )