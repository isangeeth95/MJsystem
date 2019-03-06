from django.shortcuts import render, get_object_or_404
from inventory.models import Necklaces, Earrings, Pendants, Ring
from .forms import *


def inventory(request):
    context = {
        'dashboard_dir': 'inventory'
    }
    return render(request, 'inventory/inventory.html', context)


def display_Earrings(request):
    items = Earrings.objects.all()
    context = {
        'items': items,
        'header': 'Earrings'
    }
    return render(request, 'inventory/inventory.html', context)


def display_Necklaces(request):
    items = Necklaces.objects.all()
    context = {
        'items':items,
        'header':'Necklaces',
    }
    return render(request, 'inventory/inventory.html', context)


def display_Ring(request):
    items = Ring.objects.all()
    context = {
        'items' :items,
        'header':'Rings'
    }
    return render(request, 'inventory/inventory.html', context)


def display_Pendants(request):
    items = Pendants.objects.all()
    context = {
        'items' : items,
        'header':'Pendants'
    }
    return render(request, 'inventory/inventory.html', context)



def add_Item(request, cls):
    if request.method == "POST":
        form = cls(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return render(request, 'inventory/inventory.html', {})
    else:
        form = cls()
        return render(request, 'inventory/add_newItem.html', {'form': form})


def add_Earrings(request):
    return add_Item(request, EarringForm)

def add_Necklaces(request):
    return add_Item(request, NecklacesForm)

def add_Ring(request):
    return add_Item(request, RingForm)

def add_Pendant(request):
    return add_Item(request, PendantForm)


def edit_Item(request, pk, model, cls):
    item = get_object_or_404(model, pk=pk)

    if request.method == "POST":
        form = cls(request.POST,request.FILES, instance = item)
        if form.is_valid():
            form.save()
            return render(request, 'inventory/inventory.html')
    else:
        form = cls(instance=item)
        return render(request, 'inventory/edit_item.html', {'form': form})

def edit_Earrings(request, pk):
    return edit_Item(request, pk, Earrings, EarringForm)

def edit_Necklaces(request, pk):
    return edit_Item(request, pk, Necklaces, NecklacesForm)

def edit_Ring(request, pk):
    return edit_Item(request, pk, Ring, RingForm)

def edit_Pendant(request, pk):
    return edit_Item(request, pk, Pendants, PendantForm)




def delete_Earrings(request, pk):
    Earrings.objects.filter(id=pk).delete()
    items = Earrings.objects.all()

    context={
        'items': items
    }
    return render(request, 'inventory/inventory.html')

def delete_Necklaces(request, pk):
    Necklaces.objects.filter(id=pk).delete()
    items = Necklaces.objects.all()

    context={
        'items': items
    }
    return render(request, 'inventory/inventory.html')

def delete_Ring(request, pk):
    Ring.objects.filter(id=pk).delete()
    items = Ring.objects.all()

    context={
        'items': items
    }
    return render(request, 'inventory/inventory.html')

def delete_Pendants(request, pk):
    Pendants.objects.filter(id=pk).delete()
    items = Pendants.objects.all()

    context={
        'items': items
    }
    return render(request, 'inventory/inventory.html')

