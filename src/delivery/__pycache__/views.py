from django.shortcuts import render, redirect, get_object_or_404
from.models import *
from .forms import *
from django.http import HttpResponse
import csv

def delivery(request):
    return render(request, 'delivery/delivery.html')

def staffdelivery(request):
    info = DeliveryInfo.objects.all()
    context = {'info': info,
               'dashboard_dir': 'DeliveryInfo'}
    return render(request, 'delivery/staffdelivery.html',context)

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

def staffedit_deliveryform(request, pk):
    item1 = get_object_or_404(DeliveryInfo, pk=pk)

    if request.method == "POST":
        form = StaffDelivery(request.POST, instance=item1)

        if form.is_valid():
            form.save()
            return redirect('staffdelivery')

    else:
        form = StaffDelivery(instance=item1)
        return render(request,'delivery/sedit.html',{'form': form})

def delete_deliveryform(request, pk):
    DeliveryInfo.objects.filter(pk=pk).delete()

    info = DeliveryInfo.objects.all()
    context = {'info': info}
    return render(request,'delivery/deliveryfrom.html',context)

def export_delivery_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="delivery.csv"'

    writer = csv.writer(response)
    writer.writerow(['Order_No', 'UserName', 'Receiver_Name', 'Receiver_Add', 'Telephone_No','Order_date','Deliver_date'])
    delInfo = DeliveryInfo.objects.all().values_list('Order_No', 'UserName', 'Receiver_Name', 'Receiver_Add', 'Telephone_No', 'Order_date', 'Deliver_date')
    for info in delInfo:
        writer.writerow(info)
    return response

def deliprofile(request):
    # qs = DeliveryInfo.objects.filter(UserName=request.user.get_email)
    qs1 = DeliveryInfo.objects.filter(UserName=request.user.get_email())
    Order_No = ' '
    UserName = ' '
    Receiver_Name = ' '
    Receiver_Add = ' '
    Telephone_No = ' '
    Order_date = ' '
    Deliver_date = ' '

    for d in qs1:
        Order_No = d.Order_No
        Receiver_Name = d.Receiver_Name
        Receiver_Add = d.Receiver_Add
        Telephone_No = d.Telephone_No
        Order_date = d.Order_date
        Deliver_date = d.Deliver_date

    context = {
        'qs1': qs1,
        'UserName': UserName,
        'Order_No': Order_No,
        'Receiver_Name': Receiver_Name,
        'Receiver_Add' : Receiver_Add,
        'Telephone_No' : Telephone_No,
        'Order_date' : Order_date,
        'Deliver_date' : Deliver_date,
    }
    return render(request, "delivery/deliprofile.html", context)