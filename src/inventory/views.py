from django.shortcuts import render, get_object_or_404
from .models import *
from .forms import *

def inventory(request):
    return render(request, 'inventory/inventory.html', {})

def display_Earrings(request):
    items = jewelry.objects.all()
    context = {
        'items': items,
        'header': 'Earrings'
    }
    return render(request, 'inventory/inventory.html', context)


def display_Necklaces(request):
    items = jewelry.objects.all()
    context = {
        'items':items,
        'header':'Necklaces',
    }
    return render(request, 'inventory/inventory.html', context)

def display_Ring(request):
    items = jewelry.objects.all()
    context = {
        'items' :items,
        'header':'Rings'
    }
    return render(request, 'inventory/inventory.html', context)

def display_Pendants(request):
    items = jewelry.objects.all()
    context = {
        'items' : items,
        'header':'Pendants'
    }
    return render(request, 'inventory/inventory.html', context)


#################################################################


def add_Item(request):
    if request.method == "POST":
        form = add_ItemForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return render(request, 'inventory/inventory.html', {})

    else:
        form = add_ItemForm
        return render(request, 'inventory/add_newItem.html', {'form': form})

############################################################################
def edit_items(request, pk):
    item = get_object_or_404(jewelry, pk=pk)

    if request.method == "POST":
        form = edit_ItemForm(request.POST, request.FILES, instance=item)

        if form.is_valid():
            form.save()
            return render(request, 'inventory/inventory.html', {})

    else:
        form = edit_ItemForm(instance=item)
        return render(request, 'inventory/edit_item.html', {'form': form})


def delete_items(request, pk):
    jewelry.objects.filter(pk=pk).delete()

    items = jewelry.objects.all()
    context = {'item': items}
    return render(request, 'inventory/inventory.html')