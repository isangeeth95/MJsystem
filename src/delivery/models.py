from django.db import models

# Create your models here.

class DeliveryInfo(models.Model):
    Order_No = models.CharField(max_length=6, blank=False)
    UserName = models.CharField(max_length=100)
    Receiver_Name = models.CharField(max_length=200)
    Receiver_Add = models.CharField(max_length=300)
    Telephone_No = models.IntegerField()
    Order_date = models.DateTimeField(auto_now=True)
    Deliver_date = models.DateTimeField()

    def __str__(self):
        return 'Order_No: {0} User Name:{1} Receiver_Name:{2} Receiver_Address:{3} Telephone Number:{4}'.format(
            self.Order_No, self.UserName, self.Receiver_Name, self.Receiver_Add, self.Telephone_No)