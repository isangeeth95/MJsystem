
from django.shortcuts import render,redirect, get_object_or_404
from .models import BankDetails
from .forms import *
from django.http.response import HttpResponse
import csv
import xlwt

def BussinessAccounts(request):
    context = {
        'dashboard_dir': 'BussinessAccounts'
    }
    return render(request, 'BussinessAccount/Trans.html', context)

def display_Trans(request):
    details = BankDetails.objects.all()
    context = {
        'details': details,
        'header': 'BankDetails'
    }
    return render(request, 'BussinessAccount/Trans.html', context)


def add_Trans(request):
    if request.method == "POST":
        form = TransForm(request.POST)

        if form.is_valid():
            form.save()
            return render(request, 'dashboard.html', {})
    else:
        form = TransForm
        return render(request, 'BussinessAccount/add_Trans.html', {'form': form})

def edit_Trans(request, pk):
    details = get_object_or_404(BankDetails, pk=pk)

    if request.method == "POST":
        form = TransForm (request.POST, instance=details)

        if form.is_valid():
            form.save()
            return redirect('dashboard')

    else:
        form = TransForm(instance=details)
        return render(request,'BussinessAccount/edit_Trans.html',{'form': form})


def delete_Trans(request, pk):
    BankDetails.objects.filter(pk=pk).delete()

    details = BankDetails.objects.all()
    context = {'details': details}
    return render(request,'BussinessAccount/Trans.html',context)

# Create your views here.

def export_BussinessAccounts_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="BussinessAccounts.csv"'

    writer = csv.writer(response)
    writer.writerow(['Trans_ID', ' Trans_Date', ' Bank_Name', ' Bank_Branch', 'Amount', 'Withdraw_or_Deposit', ' Trans_Type', 'Transfer_Details'])
    BussinessAccountsInfo = BankDetails.objects.all().values_list('Trans_ID', ' Trans_Date', ' Bank_Name', ' Bank_Branch', 'Amount', 'Withdraw_or_Deposit', ' Trans_Type', 'Transfer_Details')
    for info in BussinessAccountsInfo:
        writer.writerow(info)

    return response
