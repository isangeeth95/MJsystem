from django.shortcuts import render, get_object_or_404
from .models import Customer
from billing.models import BillingProfile
from order.models import Order
from delivery.models import Delivery_Address

from django.http import JsonResponse
from django.template.loader import render_to_string

# from accounts.models import online_customer

# Create your views here.

def customer_page(request):
    cus = Customer.objects.all()
    context = {
        'cus': cus,
        'dashboard_dir': 'Customer',
    }
    return render(request,'customer/customerInfo.html', context)


def customer_info(request, pk):
    cus = get_object_or_404(Customer,pk=pk)
    orderQS = None
    deliverQS = None

    try:
        bp = BillingProfile.objects.get(email=cus.email)
    except BillingProfile.DoesNotExist:
        bp = None
    if bp is not None:
        try:
            orderQS = Order.objects.filter(billing_profile=bp)
        except Order.DoesNotExist:
            orderQS = None
        try:
            deliverQS = Delivery_Address.objects.filter(billing_profile=bp)
        except Delivery_Address.DoesNotExist:
            deliverQS = None

    data = dict()
    context = {
        'customer': cus,
        'orderQS': orderQS,
        'deliverQS': deliverQS,
    }
    data['details1'] = render_to_string('customer/customerDetails.html',context)
    return JsonResponse(data)


def customer_mailing(request, email):
    return render(request,'customer/mailing.html',{'email':email})


# def customer_mailing(request): # no email
#     return render(request, 'customer/mailing.html', {'email': 'no email'})