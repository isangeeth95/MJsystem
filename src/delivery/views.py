from django.shortcuts import render, redirect, get_object_or_404
from.models import *
from .forms import *
from carts.models import Cart
from order.models import Order
from customer.models import Customer
from django.http import HttpResponse
import csv
from billing.models import BillingProfile
from django.utils.http import is_safe_url

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
    info = Delivery_Address.objects.all()
    context = {'info': info,
               'dashboard_dir': 'Delivery_Address'}
    return render(request, 'delivery/newdeliveryform.html',context)


def edit_deliveryform(request, pk):
    item = get_object_or_404(Delivery_Address, pk=pk)

    if request.method == "POST":
        form = DeliveryAddressForm(request.POST, instance=item)

        if form.is_valid():
            form.save()
            return redirect('dashboard')

    else:
        form = DeliveryAddressForm(instance=item)
        return render(request,'delivery/edit_delivery.html',{'form': form})

def edit_deliveryhistory(request, pk):
    item = get_object_or_404(Delivery_Address, pk=pk)

    if request.method == "POST":
        form = DeliveryAddressForm(request.POST, instance=item)

        if form.is_valid():
            form.save()
            return redirect('dashboard')

    else:
        form = DeliveryAddressForm(instance=item)
        return render(request,'delivery/edit_delhistory.html',{'form': form})

def delete_deliveryform(request, pk):
    Delivery_Address.objects.filter(pk=pk).delete()

    info = Delivery_Address.objects.all()
    context = {'info': info}
    return render(request,'delivery/newdeliveryform.html',context)

def staffdelivery(request):
    info = Delivery_Address.objects.all()
    context = {'info': info,
               'dashboard_dir': 'Delivery_Address'}
    return render(request, 'delivery/staffdelivery.html',context)

def staffedit_deliveryform(request, pk):
    item1 = get_object_or_404(Delivery_Address, pk=pk)

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
    qs1 = Delivery_Address.objects.filter(billing_profile=request.user.get_email())

    billing_profile = ' '
    Receiver_Name = ' '
    Receiver_Add = ' '
    District = ' '
    Delivery_Process = ' '

    for d in qs1:
        billing_profile = d.billing_profile
        Receiver_Name = d.Receiver_Name
        Receiver_Add = d.Receiver_Add
        District = d.District
        Delivery_Process = d.Delivery_Process

    context = {
        'qs1': qs1,
        'billing_profile': billing_profile,
        'Receiver_Name': Receiver_Name,
        'Receiver_Add' : Receiver_Add,
        'District' : District,
        'Delivery_Process' : Delivery_Process,
    }
    return render(request, "delivery/deliprofile.html", context)

def deliveryanalysis(request):
    qs1 = Delivery_Address.objects.all()
    qs2 = Delivery_Address.objects.all().filter(Delivery_Process='Request')
    qs3 = Delivery_Address.objects.all().filter(Delivery_Process='OnProcess')
    qs4 = Delivery_Address.objects.all().filter(Delivery_Process='onDelivery')
    qs5 = Delivery_Address.objects.all().filter(Delivery_Process='Delivered')

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


#------sangeeth-------
def checkout_delivery_address_create_view(request):
    form = DeliveryAddressForm(request.POST or None)
    error = ' '
    context = {
        'form': form,
        'error': error,
    }
    print(request.user.is_authenticated)
    next_ = request.GET.get('next')
    next_post = request.POST.get('next')
    redirect_path = next_ or next_post or None
    # redirect_path = "checkout"
    district = None

    if form.is_valid():
        print(request.POST)
        instance = form.save(commit=False)
        cart_obj, cart_created = Cart.objects.new_or_get(request)
        billing_profile, billing_profile_created = BillingProfile.objects.new_or_get(request)
        if billing_profile is not None:
            order_obj, order_obj_created = Order.objects.new_or_get(billing_profile, cart_obj)
            address_type = request.POST.get('address_type', 'delivering')
            # address_type = request.POST.get('address_type', 'billing')
            instance.billing_profile = billing_profile
            instance.order = order_obj
            instance.address_type = address_type
            instance.save()
            print(instance.Receiver_Add)
            print(instance.Receiver_Add + ", " + str(instance.District))
            delivery_obj = instance.District.net_price_district
            print(delivery_obj)
            request.session[address_type + "_address_id"] = instance.id
            request.session[address_type + "_address"] = instance.Receiver_Add + ", " + str(instance.District) + ", Sri Lanka"
            print(address_type + "_address_id")
        else:
            print("Error checkout_address_create_view function")
            return redirect("checkout")

        if is_safe_url(redirect_path, request.get_host()):
            return redirect(redirect_path)
        else:
            return redirect("checkout")
    return redirect("checkout")