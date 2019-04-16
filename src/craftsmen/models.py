from django.db import models

class craftsmen(models.Model):
    craftsmen_Item = (
    ('Earings', 'Earings'),
    ('Necklace', 'Necklace'),
    ('Ring', 'Ring'),
    ('Pendent', 'Pendent'),
)
    first_Name = models.CharField(max_length=100)  # first name of the craftsmen
    last_Name = models.CharField(max_length=100)  # last name of the craftsmen
    nic = models.CharField(max_length=10)  # NIC of the craftsmen
    address = models.CharField(max_length=400)  # address of the craftsmen
    phone_No = models.IntegerField(default=0)  # phone number
    craftsmen_Item = models.CharField(max_length=100, choices=craftsmen_Item ,blank=False)  # craftsmen item list

    def __str__(self):
        return self.first_Name
