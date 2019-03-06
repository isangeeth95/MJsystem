from django.shortcuts import render, redirect, get_object_or_404
from.models import *
from .forms import *
from django.http import HttpResponse

def delivery(request):
    return render(request, 'delivery/delivery.html')

def deliveryInfo(request):
    info = DeliveryInfo.objects.all()
    context = {'info': info,
               'dashboard_dir': 'DeliveryInfo'}
    return render(request,'delivery/deliveryfrom.html',context)

def add_deliveryform(request):
    if request.method == "POST":
        form = DeliveryForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('dashboard')

    else:
        form = DeliveryForm()
        return render(request,'delivery/add_delivery.html',{'form':form})

def edit_deliveryform(request, pk):
    item = get_object_or_404(DeliveryInfo, pk=pk)

    if request.method == "POST":
        form = DeliveryForm(request.POST, instance=item)

        if form.is_valid():
            form.save()
            return redirect('dashboard')

    else:
        form = DeliveryForm(instance=item)
        return render(request,'delivery/edit_delivery.html',{'form': form})


def delete_deliveryform(request, pk):
    DeliveryInfo.objects.filter(pk=pk).delete()

    info = DeliveryInfo.objects.all()
    context = {'info': info}
    return render(request,'delivery/deliveryfrom.html',context)