from django.shortcuts import render, redirect, HttpResponseRedirect
from .forms import LoginForm, SignUpForm
from .models import Online_Customer, User
from customer.models import Customer
from django.contrib.auth import authenticate, login, logout


# Create your views here.

# def user(request):
#     context = {
#         'dashboard_dir': 'user'
#     }
#     return render(request, 'index.html', context)


def login_page(request):
    if request.user.is_authenticated:
        return redirect('/home/')
    form = LoginForm(request.POST or None)
    error = ' '
    print(request.user.is_authenticated)
    if form.is_valid():
        print(form.cleaned_data)
        email = form.cleaned_data.get('email')
        password = form.cleaned_data.get('password')
        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            print("login success")
            if user.is_staff:
                return redirect('dashboard')
            if user.is_customer:
                return redirect('/home/')
        else:
            error = 'error'
            print('Error')

    context = {
        'form': form,
        'error': error,
    }
    return render(request, 'accounts/login.html', context)


def log_out(request):
    logout(request)
    return HttpResponseRedirect('/home/')


def signup(request):
    form = SignUpForm(request.POST or None)
    context = {
        'form': form
    }
    if form.is_valid():
        print(form.cleaned_data)
        fname = form.cleaned_data.get('fname')
        lname = form.cleaned_data.get('lname')
        email = form.cleaned_data.get('email')
        password = form.cleaned_data.get('pwd1')
        address = form.cleaned_data.get('address')
        phone = form.cleaned_data.get('phone')
        user1 = User.objects.create_customeruser(email, password) # create new auth user
        Online_Customer.objects.create(User=user1,tel_number=phone,address=address) # create online customer OneToOne with auth user
        Customer.objects.create(first_name=fname,last_name=lname,tel_number=phone,email=email)  # online customer IS-A customer, there should be validation
        return redirect("/")
    context = {
        'form': form,
        'error': form.error,
    }
    return render(request, "accounts/register.html", context)
