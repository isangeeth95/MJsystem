from django.shortcuts import render, get_object_or_404
from .models import jewelry,gold,stone,jType
from .forms import *
from django.http.response import HttpResponse
import csv
import xlwt

def inventory(request):
    return render(request, 'inventory/inventory.html', {})

def re_order(request):
    items = jewelry.objects.all()
    context = {
        'items': items,
    }
    return render(request, 'inventory/re_order.html', context)

def display_Earrings(request):
    items = jewelry.objects.all()
    context = {
        'items': items,
        'header': 'Earrings'
    }
    return render(request, 'inventory/inventory.html', context)


def display_Necklaces(request):
    items = jewelry.objects.all()
    context = {
        'items':items,
        'header':'Necklaces',
    }
    return render(request, 'inventory/inventory.html', context)

def display_Ring(request):
    items = jewelry.objects.all()
    context = {
        'items' :items,
        'header':'Rings'
    }
    return render(request, 'inventory/inventory.html', context)

def display_Pendants(request):
    items = jewelry.objects.all()
    context = {
        'items' : items,
        'header':'Pendants'
    }
    return render(request, 'inventory/inventory.html', context)

def display_Bangle(request):
    items = jewelry.objects.all()
    context = {
        'items' : items,
        'header':'Bangle'
    }
    return render(request, 'inventory/inventory.html', context)


#################################################################


def add_Item(request):
    if request.method == "POST":
        form = add_ItemForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return render(request, 'inventory/inventory.html', {})

    else:
        form = add_ItemForm
        return render(request, 'inventory/add_newItem.html', {'form': form})

############################################################################
def edit_items(request, pk):
    item = get_object_or_404(jewelry, pk=pk)

    if request.method == "POST":
        form = edit_ItemForm(request.POST, request.FILES, instance=item)

        if form.is_valid():
            form.save()
            return render(request, 'inventory/inventory.html', {})

    else:
        form = edit_ItemForm(instance=item)
        return render(request, 'inventory/edit_item.html', {'form': form})


def delete_items(request, pk):
    jewelry.objects.filter(pk=pk).delete()

    items = jewelry.objects.all()
    context = {'item': items}
    return render(request, 'inventory/inventory.html')

###################################################################################
def add_Gold(request):
    return render(request, 'inventory/add_Gold.html')

def rawMeterial(request):
    return render(request, 'inventory/rawMeterial.html')

def Gold(request):
    items = gold.objects.all()
    context = {
        'items' :items,
    }
    return render(request, 'inventory/gold.html', context)

def add_gold_submission(request):
    print ("success submit")
    code = request.POST['code']
    supplier = request.POST['supplier']
    txt = request.POST['txt']
    R = request.POST['R']
    Is = request.POST['Is']
    gBal = request.POST['gBal']
    cp = request.POST['cp']
    cd = request.POST['cd']
    bal = request.POST['bal']
    gwa = request.POST['gwa']

    goldInfo = gold(code=code,supplier=supplier,txt=txt,R=R,Is=Is,gBal=gBal,cp=cp,cd=cd,bal=bal,gwa=gwa)
    goldInfo.save()
    return render(request, 'inventory/rawMeterial.html')


def editGoldInfo(request, pk):
    item = get_object_or_404(gold, pk=pk)

    if request.method == "POST":
        form = editGoldInfoForm(request.POST, instance=item)

        if form.is_valid():
            form.save()
            return render(request, 'inventory/rawMeterial.html')

    else:
        form = editGoldInfoForm(instance=item)
        return render(request,'inventory/editGoldInfo.html',{'form': form})


def deleteGoldInfo(request, pk):
    gold.objects.filter(pk=pk).delete()

    return render(request, 'inventory/rawMeterial.html')


def export_Gold_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="gold.csv"'

    writer = csv.writer(response)
    writer.writerow(['code', 'supplier', 'txt', 'R', 'Is', 'gBal', 'cp', 'cd', 'bal', 'gwa'])
    goldInfo = gold.objects.all().values_list('code', 'supplier', 'txt', 'R', 'Is', 'gBal', 'cp', 'cd', 'bal', 'gwa')
    for info in goldInfo:
        writer.writerow(info)

    return response


def export_gold_xls(request):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="gold.xls"'
    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('gold')
    #sheet header, first row
    row_num = 0
    font_style = xlwt.XFStyle()
    font_style.font.bold = True
    columns = ['code', 'supplier', 'txt', 'R', 'Is', 'gBal', 'cp', 'cd', 'bal', 'gwa']

    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)

    #sheet body
    font_style = xlwt.XFStyle()
    rows = gold.objects.all().values_list('code', 'supplier', 'txt', 'R', 'Is', 'gBal', 'cp', 'cd', 'bal', 'gwa')
    for row in rows:
        row_num += 1
        for col_num in range(len(row)):
            ws.write(row_num, col_num, row[col_num], font_style)

    wb.save(response)
    return response


def export_jewelry_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="jewelry.csv"'

    writer = csv.writer(response)
    writer.writerow(['category', 'date', 'description', 'charges', 'stoneType', 'NoOfStones', 'weight', 'quantity', 'craftsman_id', 'issues'])
    jewelryInfo = jewelry.objects.all().values_list('category', 'date', 'description', 'charges', 'stoneType', 'NoOfStones', 'weight', 'quantity', 'craftsman_id', 'issues')
    for info in jewelryInfo:
        writer.writerow(info)

    return response



def Stone(request):
    items = stone.objects.all()
    context = {
        'items' :items,
    }
    return render(request, 'inventory/stone.html', context)

def add_stone(request):
    if request.method == "POST":
        form = stone_form(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return render(request, 'inventory/inventory.html', {})

    else:
        form = stone_form
        return render(request, 'inventory/add_newStone.html', {'form': form})


def edit_stone(request, pk):
    item = get_object_or_404(stone, pk=pk)

    if request.method == "POST":
        form = stone_form(request.POST, request.FILES, instance=item)

        if form.is_valid():
            form.save()
            return render(request, 'inventory/inventory.html', {})

    else:
        form = stone_form(instance=item)
        return render(request, 'inventory/edit_newStone.html', {'form': form})

def delete_stone_info(request, pk):
    stone.objects.filter(pk=pk).delete()

    items = stone.objects.all()
    context = {'item': items}
    return render(request, 'inventory/inventory.html')


def export_stone_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="stone.csv"'

    writer = csv.writer(response)
    writer.writerow(['name', 'supplier', 'date', 'quantity_Details', 'amount'])
    stoneInfo = stone.objects.all().values_list('name', 'supplier', 'date', 'quantity_Details', 'amount')
    for info in stoneInfo:
        writer.writerow(info)

    return response

##############################################################################################################
def add_jType(request):
    if request.method == "POST":
        form = jType_form(request.POST)

        if form.is_valid():
            form.save()
            return render(request, 'inventory/add_newStone.html', {})

    else:
        form = jType_form
        return render(request, 'inventory/add_new_jType.html', {'form': form})



