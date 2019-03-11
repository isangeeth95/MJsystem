from django.db import models
from django.contrib.auth.models import ( AbstractBaseUser, BaseUserManager, PermissionsMixin)
from customer.models import Customer


# Create your models here.
class UserManager(BaseUserManager):
    def create_user(self, email, password=None,is_active=True, is_admin=False,is_staff=False,is_customer=False):
        if not email:
            raise ValueError("User must have an email")
        if not password:
            raise ValueError("User must have a password")
        user_obj = self.model(email=self.normalize_email(email))
        user_obj.active = is_active
        user_obj.admin = is_admin
        user_obj.staff = is_staff
        user_obj.onlinecustomer = is_customer
        user_obj.set_password(password)
        user_obj.save(using=self._db)
        return user_obj

    def create_superuser(self,email,password=None):
        superuser =self.create_user(email,password=password,is_admin=True,is_staff=True)
        return superuser

    def create_staffuser(self,email,password=None):
        staffuser= self.create_user(email,password=password,is_staff=True)
        return staffuser

    def create_customeruser(self,email,password=None):
        customeruser= self.create_user(email,password=password,is_customer=True)
        return customeruser


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)
    staff = models.BooleanField(default=False)
    admin = models.BooleanField(default=False)
    onlinecustomer = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'

    objects = UserManager()

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    def get_email(self):
        return self.email

    def get_first_name(self):
        qs1 = Customer.objects.filter(email=self.email)
        for c in qs1:
            return c.first_name


    @property
    def is_active(self):
        return self.active

    @property
    def is_admin(self):
        return self.admin
    @property
    def is_staff(self):
        return self.staff

    @property
    def is_customer(self):
        return self.onlinecustomer




class Online_Customer(models.Model):
    User = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    tel_number = models.IntegerField(unique=True)
    # profile_pic = models.ImageField()
    address = models.TextField(max_length=512)


