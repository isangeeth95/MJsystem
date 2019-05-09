from django.contrib import admin
from django.contrib.auth import get_user_model
from .forms import UserAdminCreationForm, UserAdminChangeForm
from .models import Online_Customer, User, GuestEmail, StaffAcc
#from inventory.models import *



# User = get_user_model()


class UserAdmin(admin.ModelAdmin):
    search_fields = ['email']
    form = UserAdminChangeForm
    add_form = UserAdminCreationForm

    class Meta:
        model = User


admin.site.register(User, UserAdmin)
admin.site.register(Online_Customer)
admin.site.register(GuestEmail)
admin.site.register(StaffAcc)
