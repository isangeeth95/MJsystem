from django.shortcuts import render, get_object_or_404
from .models import *
#from .forms import *
from billing.models import BillingProfile
from datetime import datetime

# Create your views here.


def order(request):
    context = {
        'dashboard_dir': 'inventory'
    }
    return render(request, 'order/order.html', context)


def order_list_view(request):
    if request.user.is_admin or request.user.is_staff:
        print(request.user)
        order_list = Order.objects.all()
        context = {
            'order_list': order_list,
        }
    return render(request, "order/admin-get-order-list.html", context)


def admin_view_orders(request):
    if request.user.is_admin or request.user.is_staff:
        print(request.user)
        order_list = Order.objects.all()
        context = {
            'order_list': order_list,
        }
        return render(request, 'order/admin-get-order-list-dashboard.html', context)


def created_order_view(request):
    order = None
    if request.user.is_authenticated:
        order_id = request.POST.get('order_id')
        order = Order.objects.get(order_id=order_id)
        print("dt_object =", order.timestamp)
        print(order_id)
        print(order.cart.total)
        print(order.cart.jewelries.all())

    context = {
        "object": order,
    }
    return render(request, 'order/created-order.html', context)

