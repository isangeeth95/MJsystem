from django.db import models

# Create your models here.
class jewelry(models.Model):
    cat = models.CharField(max_length=100, blank=False)#category
    date = models.DateField()
    description = models.CharField(max_length=500, blank=False)
    charges = models.IntegerField()
    stones = models.IntegerField()
    weight = models.IntegerField()
    qty = models.IntegerField()
    craft_id = models.IntegerField()

    choices = (
        ('AVAILABLE', 'Item ready to be purchased'),
        ('SOLD', 'Item Sold'),
        ('RESTOCKING', 'Item restocking in few days')
    )

    status = models.CharField(max_length=10, choices=choices, default="SOLD")
    issues = models.CharField(max_length=100, default="No issues")

    class Meta:
        abstract = True

    def __str__(self):
        return 'cat : {0} charges : {1}'.format(self.cat, self.charges)

class Necleces(jewelry):
    pass

class Ring(jewelry):
    pass

class Pendants(jewelry):
    pass

class Earrings(jewelry):
    pass

