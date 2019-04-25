from django.db import models
from django.conf import settings
from django.db.models.signals import post_save

# Create your models here.

User = settings.AUTH_USER_MODEL

# abc@gmail.com -->> 1000 billing profiles
# user abc@gmail.com -->> 1 billing profile
class BillingProfile(models.Model):
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.PROTECT)
    email = models.EmailField()
    active = models.BooleanField(default=True)
    update = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email


def user_created_receiver(sender, instance, created, *args, **kwargs):
    if created and instance.email:
        BillingProfile.objects.get_or_create(user=instance, emai=instance.email)


post_save.connect(user_created_receiver, sender=User)



