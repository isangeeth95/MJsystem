from django.contrib import admin
#from.models import *

# Register your models here.

#
# @admin.register(DeliveryInfo)
# class ViewAdmin(admin.ModelAdmin):
#     pass

from .models import supplier
admin.site.register(supplier)