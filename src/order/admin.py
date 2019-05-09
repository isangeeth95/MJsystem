from django.contrib import admin
from .models import *


class ItemAdmin(admin.ModelAdmin):
    list_display = ['order_id', 'billing_profile', 'status', 'cart']
    class Meta:
        model = Order


admin.site.register(Order, ItemAdmin)

