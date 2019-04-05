from django.shortcuts import render, get_object_or_404
from .models import supplier
from .forms import *

def supplierInfo(request):
    sup = supplier.objects.all()
    context = {'info': sup}
    #print(sup.objects(1))
    return render(request, 'supplier/supplier.html', context)

def add_supplier(request):
    if request.method == "POST":
        form = add_supplierForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return render(request, 'dashboard.html')

    else:
        form = add_supplierForm
        return render(request, 'supplier/addSup.html', {'form': form})


def edit_supplier(request, pk):
    item = get_object_or_404(supplier, pk=pk)

    if request.method == "POST":
        form = edit_Supplier(request.POST, instance=item)

        if form.is_valid():
            form.save()
            return render(request, 'dashboard.html')

    else:
        form = edit_Supplier(instance=item)
        return render(request,'supplier/editSupplier.html',{'form': form})


def delete_Sup(request, pk):
    supplier.objects.filter(pk=pk).delete()

    info = supplier.objects.all()
    context = {'info': info}
    return render(request, 'dashboard.html')
