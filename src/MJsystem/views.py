from django.shortcuts import render, redirect
# from django.contrib.auth import get_user_model


# User = get_user_model()

def test_page(request):
    return render(request, 'base.html', {})


def index_page(request):
    return render(request, 'index.html', {})


def home_page(request):
    return render(request, 'home_home.html', {})


def dashboard(request):
    if not request.user.is_staff:
        return redirect('/user/login')
    context ={
        'user_name': request.user.get_email()
    }
    return render(request, 'dashboard.html', context)
