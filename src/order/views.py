from django.shortcuts import render, get_object_or_404
from .models import *
#from .forms import *

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

