from django.contrib import admin
from .models import Necklaces, Ring, Pendants, Earrings, jewelry
# Register your models here.


class RingAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'slug']

    class Meta:
        model = jewelry


admin.site.register(Necklaces)
admin.site.register(Ring, RingAdmin)
admin.site.register(Pendants)
admin.site.register(Earrings)

