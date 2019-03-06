from django.shortcuts import render
from .models import Customer
# from accounts.models import online_customer

# Create your views here.

def customer_page(request):
    cus = Customer.objects.all()
    context = {
        'cus': cus,
        'dashboard_dir': 'Customer',
    }
    return render(request,'customer/customerInfo.html', context)
