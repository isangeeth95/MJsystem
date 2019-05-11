from django.db import models
from billing.models import BillingProfile

# Create your models here.
class DeliveryDistance(models.Model):
    Destination = models.CharField(max_length=100)
    Distance = models.IntegerField()
    Price = models.FloatField()

    def __str__(self):
        return format(self.Destination)

    @property
    def net_price_district(self):
        return self.Distance * self.Price

class DeliveryInfo(models.Model):
    deliveryProcess = (
        ('Request', 'Request'),
        ('OnProcess', 'Processing'),
        ('onDelivery', 'on Delivery'),
        ('Delivered', 'Delivered')
    )

    Order_No = models.CharField(max_length=6, blank=False,)
    UserName = models.CharField(max_length=100)
    Receiver_Name = models.CharField(max_length=200)
    Receiver_Add = models.CharField(max_length=300)
    District = models.ForeignKey(DeliveryDistance, on_delete=models.CASCADE, null=True)
    Telephone_No = models.IntegerField()
    Order_date = models.DateTimeField(auto_now=True)
    Deliver_date = models.DateTimeField()
    Delivery_Process = models.CharField(max_length=100, choices=deliveryProcess, default='Request')

    def __str__(self):
        return 'Order_No: {0} User Name:{1} Receiver_Name:{2} Receiver_Address:{3}  Telephone Number:{4} Order_date:{5} Deliver_date:{6} Delivery_Process:{7}'.format(
            self.Order_No, self.UserName, self.Receiver_Name, self.Receiver_Add, self.Telephone_No, self.Order_date, self.Deliver_date, self.Delivery_Process)


#---------sangeeth-------------

ADDRESS_TYPES = (
    ('delivering', 'Delivering'),
)


class Delivery_Address(models.Model):
    billing_profile = models.ForeignKey(BillingProfile, on_delete=models.PROTECT)
    address_type = models.CharField(max_length=120, choices=ADDRESS_TYPES)
    Receiver_Name = models.CharField(max_length=200)
    Receiver_Add = models.CharField(max_length=300)
    District = models.ForeignKey(DeliveryDistance, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return str(self.billing_profile)

    def get_address(self):
        return "{Receiver_Name}\n,{Receiver_Add}\n{District}\n{country}\n".format(
            Receiver_Name=self.Receiver_Name,
            Receiver_Add=self.Receiver_Add,
            District=self.District,
            country="Sri Lanka",
        )
