from django.shortcuts import render
from django.views.generic import ListView
from inventory.models import jewelry , Necklaces, Ring

# Create your views here.

def Product_List_View(request):
    querySet = Ring.objects.all()
    context = {
        'qs': querySet
    }
    return render(request, "Products/product_list.html", context)
