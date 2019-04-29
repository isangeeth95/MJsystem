from django.db import models

# Create your models here.

class DeliveryInfo(models.Model):
    deliveryProcess = (
        ('Request', 'Request'),
        ('OnProcess', 'Processing'),
        ('onDelivery', 'on Delivery'),
        ('Delivered', 'Delivered')
    )

    districts = (
        ('Colombo', 'Colombo'),
        ('Gampaha', 'Gampaha'),
        ('Kalutara', 'Kalutara'),
        ('Kandy', 'Kandy')
    )
    Order_No = models.CharField(max_length=6, blank=False,)
    UserName = models.CharField(max_length=100)
    Receiver_Name = models.CharField(max_length=200)
    Receiver_Add = models.CharField(max_length=300)
    District = models.CharField(max_length=100, choices=districts, blank=False,)
    Telephone_No = models.IntegerField()
    Order_date = models.DateTimeField(auto_now=True)
    Deliver_date = models.DateTimeField()
    Delivery_Process = models.CharField(max_length=100, choices=deliveryProcess, default='Request')

    def __str__(self):
        return 'Order_No: {0} User Name:{1} Receiver_Name:{2} Receiver_Address:{3} District:{4} Telephone Number:{5} Order_date:{6} Deliver_date:{7} Delivery_Process:{8}'.format(
            self.Order_No, self.UserName, self.Receiver_Name, self.Receiver_Add, self.District, self.Telephone_No, self.Order_date, self.Deliver_date, self.Delivery_Process)

class DeliveryDistance(models.Model):
    Destination = models.CharField(max_length=100)
    Distance = models.IntegerField()
    Price = models.FloatField()

    @property
    def net_price_district(self):
        return self.Distance * self.Price

    def __str__(self):
        return 'Destination:{0} Distance:{1} Price:{2}'.format(self.Destination, self.Distance, self.Price)
