from django.shortcuts import render, get_object_or_404
from .models import *
from .forms import *

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
        return render(request, 'supplier/addSup.html', {'form': form})


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
