from django.shortcuts import render, get_object_or_404,redirect
from .models import *
from .forms import *
import csv
from django.http.response import HttpResponse

def craftsmenInfo(request):
    sup = craftsmen.objects.all()
    context = {'info': sup}
    #print(sup.objects(1))
    return render(request, 'craftsmen/craftsmen.html', context)

def add_craftsmen(request):
    if request.method == "POST":
        form = add_craftsmenForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return render(request, 'dashboard.html')

    else:
        form = add_craftsmenForm
        return render(request, 'craftsmen/add_craftsmen.html', {'form': form})


def editcraftsmen(request, pk):
    item = get_object_or_404(craftsmen, pk=pk)

    if request.method == "POST":
        form = edit_craftsmen(request.POST, instance=item)

        if form.is_valid():
            form.save()
            return render(request, 'dashboard.html')

    else:
        form = edit_craftsmen(instance=item)
        return render(request,'craftsmen/editcraftsmen.html',{'form': form})


def delete_craftsmen(request, pk):
    craftsmen.objects.filter(pk=pk).delete()

    info = craftsmen.objects.all()
    context = {'info': info}
    return render(request, 'dashboard.html')

def export_craftsmen_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="craftsmen.csv"'

    writer = csv.writer(response)
    writer.writerow(['first_Name', 'last_Name', 'nic', 'address', 'phone_No', 'craftsmen_Item'])
    craftsmenInfo = craftsmen.objects.all().values_list('first_Name', 'last_Name', 'nic', 'address', 'phone_No', 'craftsmen_Item')
    for info in craftsmenInfo:
        writer.writerow(info)

    return response

def requestJewelryForm(request):
    if request.method == "POST":
        form = requestedJewelryForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect("/dashboard")

    else:
        form = requestedJewelryForm
        return render(request, 'craftsmen/requestedJewelryform.html', {'form': form})

def requestJewelry(request):
    sup = requestedJewelry.objects.all()
    context = {'info': sup}
    #print(sup.objects(1))
    return render(request, 'craftsmen/requestedJewelry.html', context)