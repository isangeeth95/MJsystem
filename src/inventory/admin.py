from django.contrib import admin
from .models import  *

class RingAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'slug']
    class Meta:
        model = jewelry

admin.site.register(jewelry)
admin.site.register(gold)