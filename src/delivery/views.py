from django.shortcuts import render, redirect, get_object_or_404
from.models import *
from .forms import *
from customer.models import Customer
from django.http import HttpResponse
import csv

def delivery(request):
    return render(request, 'delivery/delivery.html')

def mainstaffpage(request):
    return render(request, 'delivery/staffchoice.html')

def addarea(request):
    if request.method == "POST":
        form = DeliveyDistanceForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('displayAreas')

    else:
        form = DeliveyDistanceForm()
        return render(request, 'delivery/add_delivery_areas.html',{'form':form})

def displayAreas(request):
    info1 = DeliveryDistance.objects.all()
    context = {'info1' : info1,
               'dashboard_dir': 'DeliveryDistance'}
    return render(request,'delivery/areafrom.html',context)

def edit_deliveryArea(request, pk):
    item2 = get_object_or_404(DeliveryDistance, pk=pk)

    if request.method == "POST":
        form = DeliveyDistanceForm(request.POST, instance=item2)

        if form.is_valid():
            form.save()
            return redirect('displayAreas')

    else:
        form = DeliveyDistanceForm(instance=item2)
        return render(request,'delivery/edit_deliveryArea.html',{'form': form})

def delete_deliveryArea(request, pk):
    DeliveryDistance.objects.filter(pk=pk).delete()

    info1 = DeliveryDistance.objects.all()
    context = {'info1': info1}
    return render(request,'delivery/areafrom.html',context)


def deliveryInfo(request):
    info = DeliveryInfo.objects.all()
    context = {'info': info,
               'dashboard_dir': 'DeliveryInfo'}
    return render(request,'delivery/deliveryfrom.html',context)

def add_deliveryform(request):
    haa = get_object_or_404(Customer, email=request.user.email)
    init = {
        'UserName': haa.email,
    }
    if request.method == "POST":
        form = DeliveryForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('dashboard')

    else:
        form = DeliveryForm(initial=init)
        return render(request, 'delivery/add_delivery.html', {'form': form})

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

def edit_deliveryhistory(request, pk):
    item = get_object_or_404(DeliveryInfo, pk=pk)

    if request.method == "POST":
        form = DeliveryForm(request.POST, instance=item)

        if form.is_valid():
            form.save()
            return redirect('dashboard')

    else:
        form = DeliveryForm(instance=item)
        return render(request,'delivery/edit_delhistory.html',{'form': form})

def delete_deliveryform(request, pk):
    DeliveryInfo.objects.filter(pk=pk).delete()

    info = DeliveryInfo.objects.all()
    context = {'info': info}
    return render(request,'delivery/deliveryfrom.html',context)

def staffdelivery(request):
    info = DeliveryInfo.objects.all()
    context = {'info': info,
               'dashboard_dir': 'DeliveryInfo'}
    return render(request, 'delivery/staffdelivery.html',context)

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

def deliveryanalysis(request):
    qs1 = DeliveryInfo.objects.all()
    qs2 = DeliveryInfo.objects.all().filter(Delivery_Process='Request')
    qs3 = DeliveryInfo.objects.all().filter(Delivery_Process='OnProcess')
    qs4 = DeliveryInfo.objects.all().filter(Delivery_Process='onDelivery')
    qs5 = DeliveryInfo.objects.all().filter(Delivery_Process='Delivered')

    numberOfRequest = qs1.count()
    numberOfDelRequest = qs2.count()
    numberOfDelProcess = qs3.count()
    numberOfDelOndelivery = qs4.count()
    numberOfDelDelivered = qs5.count()

    context ={
        'numberOfRequest' : numberOfRequest,
        'numberOfDelRequest' : numberOfDelRequest,
        'numberOfDelProcess' : numberOfDelProcess,
        'numberOfDelOndelivery': numberOfDelOndelivery,
        'numberOfDelDelivered' : numberOfDelDelivered,
    }

    return render(request, 'delivery/analyst.html', context)