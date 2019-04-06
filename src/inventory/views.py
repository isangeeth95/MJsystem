from django.shortcuts import render, get_object_or_404
from .models import jewelry,gold
from .forms import *

def inventory(request):
    return render(request, 'inventory/inventory.html', {})

def re_order(request):
    items = jewelry.objects.all()
    context = {
        'items': items,
    }
    return render(request, 'inventory/re_order.html', context)

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

###################################################################################
def add_Gold(request):
    return render(request, 'inventory/add_Gold.html')

def rawMeterial(request):
    return render(request, 'inventory/rawMeterial.html')

def Gold(request):
    items = gold.objects.all()
    context = {
        'items' :items,
    }
    return render(request, 'inventory/gold.html', context)

def add_gold_submission(request):
    print ("success submit")
    code = request.POST['code']
    supplier = request.POST['supplier']
    txt = request.POST['txt']
    R = request.POST['R']
    Is = request.POST['Is']
    gBal = request.POST['gBal']
    cp = request.POST['cp']
    cd = request.POST['cd']
    bal = request.POST['bal']
    gwa = request.POST['gwa']

    goldInfo = gold(code=code,supplier=supplier,txt=txt,R=R,Is=Is,gBal=gBal,cp=cp,cd=cd,bal=bal,gwa=gwa)
    goldInfo.save()
    return render(request, 'inventory/rawMeterial.html')


def editGoldInfo(request, pk):
    item = get_object_or_404(gold, pk=pk)

    if request.method == "POST":
        form = editGoldInfoForm(request.POST, instance=item)

        if form.is_valid():
            form.save()
            return render(request, 'inventory/rawMeterial.html')

    else:
        form = editGoldInfoForm(instance=item)
        return render(request,'inventory/editGoldInfo.html',{'form': form})


def deleteGoldInfo(request, pk):
    gold.objects.filter(pk=pk).delete()

    return render(request, 'inventory/rawMeterial.html')

