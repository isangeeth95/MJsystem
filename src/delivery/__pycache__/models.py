from django.db import models

# Create your models here.

class DeliveryInfo(models.Model):
    deliveryProcess = (
        ('Request', 'Request'),
        ('OnProcess', 'Processing'),
        ('onDelivery', 'on Delivery'),
        ('Delivered', 'delivered')
    )

    Order_No = models.CharField(max_length=6, blank=False,)
    UserName = models.CharField(max_length=100)
    Receiver_Name = models.CharField(max_length=200)
    Receiver_Add = models.CharField(max_length=300)
    Telephone_No = models.IntegerField()
    Order_date = models.DateTimeField(auto_now=True)
    Deliver_date = models.DateTimeField()
    Delivery_Process = models.CharField(max_length=100, choices=deliveryProcess, default='Request')

    def __str__(self):
        return 'Order_No: {0} User Name:{1} Receiver_Name:{2} Receiver_Address:{3} Telephone Number:{4} Order_date:{5} Deliver_date:{6} Delivery_Process:{7}'.format(
            self.Order_No, self.UserName, self.Receiver_Name, self.Receiver_Add, self.Telephone_No, self.Order_date, self.Deliver_date, self.Delivery_Process)

class DeliveryPrice(models.Model):
    Destination = models.CharField(max_length=100)
    Distance = models.IntegerField()
    UnitPrice = models.FloatField()
    TotalPrice = models.FloatField()

    def __str__(self):
        return 'Destination:{0} Distance:{1} UnitPrice:{2} TotalPrice:{3}'.format(self.Destination, self.Distance, self.UnitPrice, self.TotalPrice)
