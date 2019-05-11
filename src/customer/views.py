from django.shortcuts import render, get_object_or_404
from .models import Customer
from billing.models import BillingProfile
from order.models import Order

from django.http import JsonResponse
from django.template.loader import render_to_string

# from accounts.models import online_customer

# Create your views here.

def customer_page(request):
    cus = Customer.objects.all()
    context = {
        'cus': cus,
        'dashboard_dir': 'Customer',
        'orders': Order.objects.all()
    }
    return render(request,'customer/customerInfo.html', context)


def customer_info(request, pk):
    cus = get_object_or_404(Customer,pk=pk)
    data = dict()
    data['details1'] = render_to_string('customer/customerDetails.html',{'customer': cus})
    return JsonResponse(data)
