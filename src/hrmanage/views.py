from django.shortcuts import render,redirect, get_object_or_404
from .models import Staff
from .forms import *
from django.http import HttpResponse
import csv

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
    return render(request,'hr/staff.html',context)


def export_Staff_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="Staff.csv"'

    writer = csv.writer(response)
    writer.writerow(['Emp_ID', 'First_Name', 'Last_Name', 'Email', 'Phone_Number','Admission_date','Job_title','Job_level'])
    staffInfo = Staff.objects.all().values_list('Emp_ID', 'First_Name', 'Last_Name', 'Email', 'Phone_Number','Admission_date','Job_title','Job_level')
    for info in staffInfo:
        writer.writerow(info)
    return response