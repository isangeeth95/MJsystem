from django.shortcuts import render,redirect, get_object_or_404
from .models import Staff
from .forms import *
from django.http import HttpResponse

def hrmanage(request):
    context = {
        'dashboard_dir': 'hrmanage'
    }
    return render(request, 'hr/staff.html', context)

def display_Staff(request):
    details = Staff.objects.all()
    context = {
        'details': details,
        'header': 'Staff'
    }
    return render(request, 'hr/staff.html', context)


def add_Staff(request):
    if request.method == "POST":
        form = StaffForm(request.POST)

        if form.is_valid():
            form.save()
            return render(request, 'dashboard.html', {})
    else:
        form = StaffForm
        return render(request, 'hr/add_staff.html', {'form': form})

def edit_staff(request, pk):
    details = get_object_or_404(Staff, pk=pk)

    if request.method == "POST":
        form = StaffForm(request.POST, instance=details)

        if form.is_valid():
            form.save()
            return redirect('dashboard')

    else:
        form = StaffForm(instance=details)
        return render(request,'hr/edit_staff.html',{'form': form})


def delete_staff(request, pk):
    Staff.objects.filter(pk=pk).delete()

    details = Staff.objects.all()
    context = {'details': details}
    return render(request,'staff.html',context)