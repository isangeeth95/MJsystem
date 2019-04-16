import random
import os
from django.db import models
from craftsmen.models import *
from supplier.models import *
from django.forms import ModelForm
from django.utils.timezone import datetime
from .utils import unique_slug_generator
from django.db.models.signals import pre_save, post_save

def get_filename_ext(filename):
    base_name = os.path.basename(filename)
    name, ext = os.path.splitext(filename)
    return name, ext

def upload_image_path(instance, filename):
    print(instance)
    print(filename)
    new_filename = random.randint(1, 10000000)
    name, ext = get_filename_ext(filename)
    final_filename = '{new_filename}{ext}'.format(new_filename=new_filename, ext=ext)
    return "jewelry_image/{new_filename}/{final_filename}".format(new_filename=new_filename,
                                                                  final_filename=final_filename)

class gold(models.Model):

    code = models.IntegerField()#number
    supplier = models.CharField(max_length=500, blank=False) #name of the supplier
    txt = models.DateField(default=datetime.now, blank=False) #date of the purchased
    R = models.CharField(max_length=500, blank=False) #recived gold weight
    Is = models.CharField(max_length=500, blank=False) #gold weight which issued by shop
    gBal = models.CharField(max_length=500, blank=False) # gold weight balance
    cp = models.FloatField() #payed amount
    cd = models.FloatField() #amount to pay
    bal = models.FloatField() #amount balance
    gwa = models.CharField(max_length=500, blank=False) #gold weight amount at the year


##########################################################################################
class jType(models.Model):
    jtype=models.CharField(max_length=100)

    def __str__(self):
        return format(self.jtype)
##########################################################################################
class stone(models.Model):
    name=models.CharField(max_length=100)
    supplier=models.ForeignKey(supplier, on_delete=models.CASCADE, null=True)
    date = models.DateField(default=datetime.now, blank=True)
    quantity_Details=models.CharField(max_length=500, blank=True)
    amount=models.FloatField(null=True, blank=True)

    def __str__(self):
        return format(self.name)
##########################################################################################
class jewelry(models.Model):

    category = models.ForeignKey(jType, on_delete=models.CASCADE, null=True)
    slug = models.SlugField(blank=True, unique=True)
    date = models.DateField(default=datetime.now, blank=True)
    description = models.CharField(max_length=500, blank=True)
    charges = models.FloatField()
    stoneType = models.ForeignKey(stone, on_delete=models.CASCADE, null=True)
    NoOfStones = models.IntegerField()
    weight = models.FloatField()
    quantity = models.IntegerField()
    craftsman_id = models.ForeignKey(craftsmen, on_delete=models.CASCADE, null=True)

    choices = (
        ('AVAILABLE', 'Item ready to be purchased'),
        ('SOLD', 'Item Sold'),
        ('RESTOCKING', 'Item restocking in few days')
    )
    status = models.CharField(max_length=10, choices=choices, default="AVAILABLE")
    issues = models.CharField(max_length=100, default="No issues")
    image = models.ImageField(upload_to='jewelry_image/', null=True, blank=True)

    # class Meta:
    #     abstract = True

    @property
    def net_price(self):
        return self.charges * 50

    @property
    def total_net_price(self):
        return self.quantity *  self.net_price

    def get_absolute_url(self):
        return "/products/list/{slug}/".format(slug=self.slug)


    def __str__(self):
        return 'cat : {0} charges : {1}'.format(self.category, self.charges)

def ring_presave_receiver(sender, instance, *args, **kwargs):

    if not instance.slug:
        instance.slug = 'abc'
        pre_save.connect(ring_presave_receiver, sender=jewelry)

