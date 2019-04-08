from django.shortcuts import render, redirect, HttpResponseRedirect, get_object_or_404
from .forms import LoginForm, SignUpForm, EditProfile
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
                return redirect('/')
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
    return HttpResponseRedirect('/')


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST, request.FILES)
        print('image url')
        print(form.is_valid())
        #print(form.cleaned_data.get('image'))
        if form.is_valid():
            print('in valid form')
            print(form.cleaned_data)
            fname = form.cleaned_data.get('fname')
            lname = form.cleaned_data.get('lname')
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('pwd1')
            address = form.cleaned_data.get('address')
            phone = form.cleaned_data.get('phone')
            image = form.cleaned_data.get('user_image')
            user1 = User.objects.create_customeruser(email, password) # create new auth user
            Online_Customer.objects.create(User=user1,tel_number=phone,address=address,profile_pic=image) # create online customer OneToOne with auth user
            Customer.objects.create(first_name=fname,last_name=lname,tel_number=phone,email=email)  # online customer IS-A customer, there should be validation
            return redirect("/")
    else:
        form = SignUpForm()
    context = {
        'form': form,
        'error': form.error,
    }
    return render(request, "accounts/register.html", context)


def profile(request):
    qs = Online_Customer.objects.filter(User=request.user)
    qs1 = Customer.objects.filter(email=request.user.get_email())
    email = ' '
    fname = ' '
    lname = ' '
    address = ' '
    tel = ' '
    for c in qs:
        address = c.address
        tel = c.tel_number
        pic = c.profile_pic.url
    for c1 in qs1:
        print(c1.email)
        email = c1.email
        fname = c1.first_name
        lname = c1.last_name
    context = {
        'username': fname + ' ' + lname,
        'email': email,
        'address': address,
        'tel' : tel,
        'picture' : pic,
    }
    return render(request, "accounts/profile.html", context)

def settings(request):
    cus = get_object_or_404(Customer, email=request.user.email)
    online_cus = get_object_or_404(Online_Customer, tel_number=cus.tel_number)



    if request.method == "POST":
        profile_form = EditProfile(request.POST)
        if profile_form.is_valid():
            fname = profile_form.cleaned_data.get('fname')
            lname = profile_form.cleaned_data.get('lname')
            address = profile_form.cleaned_data.get('address')
            phone = profile_form.cleaned_data.get('phone')
            print(fname + ' ' + lname + ' '+ address)
            cus.first_name = fname
            cus.last_name = lname
            cus.tel_number = phone
            cus.save()
            online_cus.tel_number = phone
            online_cus.address = address
            online_cus.save()


        return redirect('/')
    else:
        profile_form = EditProfile()

    context = {
        'form': profile_form,
        'fname': cus.first_name,
        'lname' : cus.last_name,
        'address': online_cus.address,
        'phone':online_cus.tel_number,
    }

    return render(request,"accounts/profile_settings.html",context)