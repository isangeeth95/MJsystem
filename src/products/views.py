from django.shortcuts import render
from django.views.generic import ListView
from inventory.models import jewelry , Necklaces, Ring

# Create your views here.

def Product_List_View(request):
    querySet = Ring.objects.all()
    set=Necklaces.objects.all();
    context = {
        'qs': querySet,
        'qs1': set
    }
    return render(request, "Products/product_list.html", context)
