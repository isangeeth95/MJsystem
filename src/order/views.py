from django.shortcuts import render, get_object_or_404
from .models import *
#from .forms import *

# Create your views here.


def order(request):
    context = {
        'dashboard_dir': 'inventory'
    }
    return render(request, 'order/order.html', context)

