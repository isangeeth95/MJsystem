from django.shortcuts import render


def test_page(request):
    return render(request, 'base.html', {})


def home_page(request):
    return render(request, 'index.html', {})


def dashboard(request):
    return render(request, 'dashboard.html', {})
