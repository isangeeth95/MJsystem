from django.contrib import admin
#from.models import *

# Register your models here.

#
# @admin.register(DeliveryInfo)
# class ViewAdmin(admin.ModelAdmin):
#     pass

from .models import *
admin.site.register(DeliveryInfo)
admin.site.register(DeliveryDistance)
