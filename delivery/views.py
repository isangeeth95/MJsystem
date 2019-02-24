from django.shortcuts import render

def delivery(request):
    context = {
        'dashboard_dir': 'Delivery'  # dashboard/customer
    }
    return render(request, 'delivery.html', context)
