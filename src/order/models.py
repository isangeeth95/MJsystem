import math
from django.db import models
from MJsystem.utils import unique_order_id_generator, unique_slug_generator
from django.db.models.signals import pre_save, post_save
from carts.models import Cart
from addresses.models import Address
from billing.models import BillingProfile

ORDER_STATUS_CHOICES = (
    ('created', 'Created'),
    ('paid', 'Paid'),
    ('delivered', 'Delivered'),
    ('refunded', 'Refunded')
)


class OrderManager(models.Manager):
    def new_or_get(self, billing_profile, cart_obj):
        created = False
        qs = self.get_queryset().filter(
            billing_profile=billing_profile,
            cart=cart_obj,
            active=True,
            # status=created,
        )

        if qs.count() == 1:
            obj = qs.first()

        else:
            obj = self.model.objects.create(
                billing_profile=billing_profile,
                cart=cart_obj
            )
            created = True

        return obj, created


class Order(models.Model):
    billing_profile = models.ForeignKey(BillingProfile, null=True, blank=True, on_delete=models.PROTECT)
    order_id = models.CharField(max_length=120, blank=True)
    delivering_address = models.CharField(max_length=200, null=True, blank=True)
    billing_address = models.ForeignKey(Address, related_name="billing_address", null=True, blank=True, on_delete=models.PROTECT)
    cart = models.ForeignKey(Cart, on_delete=models.PROTECT)
    status = models.CharField(max_length=120, default='created', choices=ORDER_STATUS_CHOICES)
    delivering_total = models.DecimalField(default=50.00, max_digits=100, decimal_places=2)
    total = models.DecimalField(default=0.00, max_digits=100, decimal_places=2)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.order_id

    objects = OrderManager()

    def update_total(self):
        cart_total = self.cart.total
        delivering_total = self.delivering_total
        new_total = math.fsum([cart_total, delivering_total])
        self.total = new_total
        self.save()
        return new_total

    def check_done(self):
        billing_profile = self.billing_profile
        delivering_address = self.delivering_address
        billing_address = self.billing_address
        total = self.total
        print("inside the check done function")
        print(billing_profile)
        print(billing_address)
        print(total)
        print(delivering_address)
        if (billing_address and billing_profile and total > 0) or (billing_address and billing_profile and total > 0
                                                                   and delivering_address):
            print("returning check done true")
            return True
        else:
            print("returning check done false")
            return False

    def mark_paid(self):
        if self.check_done():
            self.status = "paid"
            self.save()
        return self.status

    def assign_delivering_address_to_none(self):
        print("inside the assign_delivering_address_to_none function")
        delivering_address = "None"
        self.delivering_address = delivering_address
        self.save()
        return self.delivering_address


def pre_save_create_order_id(sender, instance, *args, **kwargs):
    if not instance.order_id:
        instance.order_id = unique_order_id_generator(instance)
        # instance.order_id = unique_slug_generator(instance)
    qs = Order.objects.filter(cart=instance.cart).exclude(billing_profile=instance.billing_profile)
    if qs.exists():
        qs.update(active=False)


pre_save.connect(pre_save_create_order_id, sender=Order)


def post_save_cart_total(sender, instance, created, *args, **kwargs):
    if not created:
        cart_obj = instance
        cart_total = cart_obj.total
        cart_id = cart_obj.id
        qs = Order.objects.filter(cart__id=cart_id)
        if qs.count() == 1:
            order_obj = qs.first()
            order_obj.update_total()


post_save.connect(post_save_cart_total, sender=Cart)


def post_save_order(sender, instance, created, *args, **kwargs):
    print("Running")
    if created:
        print("Updating First")
        instance.update_total()


post_save.connect(post_save_order, sender=Order)