from django.shortcuts import render, get_object_or_404,redirect
from .models import Customer
from .form import EmailForm

from billing.models import BillingProfile
from order.models import Order
from delivery.models import Delivery_Address
from django.core.mail import send_mail
from MJsystem.settings import EMAIL_HOST_USER

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
    if request.method == 'POST':
        emailform = EmailForm(request.POST)
        if emailform.is_valid():
            To = emailform.cleaned_data.get('To')
            sub = emailform.cleaned_data.get('subject')
            mas = emailform.cleaned_data.get('mass')
            send_mail(sub,mas,EMAIL_HOST_USER,[To],fail_silently=False)
            return redirect("/")
    else:
        emailform = EmailForm(initial={'To': email})

    data = dict()
    context = {
        'email':emailform,
    }
    data['details1'] = render_to_string('customer/mailing.html', context, request=request)
    return JsonResponse(data)


# def customer_mailing(request): # no email
#     return render(request, 'customer/mailing.html', {'email': 'no email'})