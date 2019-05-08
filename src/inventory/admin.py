from django.contrib import admin
from .models import  *

class ItemAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'slug']
    class Meta:
        model = jewelry

admin.site.register(jewelry, ItemAdmin)
admin.site.register(gold)
admin.site.register(jType)
admin.site.register(stone)