import random
import os
from django.db import models
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



class jewelry(models.Model):

    catChoice =(
        ('NE', 'Necklaces'),
        ('RI', 'Ring'),
        ('PE', 'Pendants'),
        ('ER', 'Earrings')
    )

    category = models.CharField(max_length=100, choices=catChoice ,blank=False )#category
    slug = models.SlugField(blank=True, unique=True)
    date = models.DateField(default=datetime.now, blank=True)
    description = models.CharField(max_length=500, blank=False)
    charges = models.FloatField()
    stoneType = models.CharField(max_length=100, blank=False)
    NoOfStones = models.IntegerField()
    weight = models.FloatField()
    quantity = models.IntegerField()
    craftsman_id = models.IntegerField()

    choices = (
        ('AVAILABLE', 'Item ready to be purchased'),
        ('SOLD', 'Item Sold'),
        ('RESTOCKING', 'Item restocking in few days')
    )
    status = models.CharField(max_length=10, choices=choices, default="SOLD")
    issues = models.CharField(max_length=100, default="No issues")
    image = models.ImageField(upload_to='jewelry_image/', null=True, blank=False)

    # class Meta:
    #     abstract = True

    def get_absolute_url(self):
        return "/products/list/{slug}/".format(slug=self.slug)


    def __str__(self):
        return 'cat : {0} charges : {1}'.format(self.category, self.charges)


def ring_presave_receiver(sender, instance, *args, **kwargs):

    if not instance.slug:
        instance.slug = 'abc'


pre_save.connect(ring_presave_receiver, sender=jewelry)


