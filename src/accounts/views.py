from django.shortcuts import render, redirect, HttpResponseRedirect, get_object_or_404
from .forms import LoginForm, SignUpForm, EditProfile, deleteProfile, GuestForm
from .models import Online_Customer, User, GuestEmail
from customer.models import Customer
from billing.models import BillingProfile
from order.models import Order
from delivery.models import Delivery_Address
from django.contrib.auth import authenticate, login, logout
from django.utils.http import is_safe_url
from datetime import datetime

# Create your views here.

# def user(request):
#     context = {
#         'dashboard_dir': 'user'
#     }
#     return render(request, 'index.html', context)


#sangeeth added below function
def guest_register_view(request):
    form = GuestForm(request.POST or None)
    error = ' '
    context = {
        'form': form,
        'error': error,
    }
    print(request.user.is_authenticated)
    next_ = request.GET.get('next')
    next_post = request.POST.get('next')
    redirect_path = next_ or next_post or None

    if form.is_valid():
        print(form.cleaned_data)
        email = form.cleaned_data.get('email')
        new_guest_email = GuestEmail.objects.create(email=email)
        request.session['guest_email_id'] = new_guest_email.id
        if is_safe_url(redirect_path, request.get_host()):
            return redirect(redirect_path)
        else:
            return redirect("/register/")
    return redirect("/register/")


def login_page(request):
    if request.user.is_authenticated:
        return redirect('/home/')
    form = LoginForm(request.POST or None)
    error = ' '
    print(request.user.is_authenticated)
    # sangeeth added bellow lines
    next_ = request.GET.get('next')
    next_post = request.POST.get('next')
    redirect_path = next_ or next_post or None
    #til this

    if form.is_valid():
        print(form.cleaned_data)
        email = form.cleaned_data.get('email')
        password = form.cleaned_data.get('password')
        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            print("login success")
            try:
                del request.session['guest_email_id']
            except:
                pass
            if user.is_staff:
                return redirect('dashboard')
            if user.is_customer:
                #sangeeth added below lines
                if is_safe_url(redirect_path, request.get_host()):
                    return redirect(redirect_path)
                #till this
                else:
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
        # print(form.cleaned_data.get('image'))
        if form.is_valid():
            print('valid form')
            print(form.cleaned_data)
            fname = form.cleaned_data.get('fname')
            lname = form.cleaned_data.get('lname')
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('pwd1')
            address = form.cleaned_data.get('address')
            phone = form.cleaned_data.get('phone')
            image = form.cleaned_data.get('user_image')
            user1 = User.objects.create_customeruser(email, password)  # create new auth user
            Online_Customer.objects.create(User=user1, tel_number=phone, address=address,
                                           profile_pic=image)  # create online customer OneToOne with auth user
            Customer.objects.create(first_name=fname, last_name=lname, tel_number=phone,
                                    email=email)  # online customer IS-A customer, there should be validation
            return redirect("/")
    else:
        form = SignUpForm()
    context = {
        'form': form,
        'error': form.error,
    }
    return render(request, "accounts/register.html", context)


def profile(request):
    context = {
        'username': 'Admin',
        'email': request.user.get_email,
    }
    if request.user.is_customer:
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

        orderQS = None
        deliverQS = None

        try:
            bp = BillingProfile.objects.get(user=request.user)
        except BillingProfile.DoesNotExist:
            bp = None
        if bp is not None:
            try:
                orderQS = Order.objects.filter(billing_profile=bp)
            except Order.DoesNotExist:
                orderQS = None
            try:
                deliverQS = Delivery_Address.objects.filter(billing_profile=bp)
            except Delivery_Address.DoesNotExist:
                deliverQS = None

        context = {
            'username': fname + ' ' + lname,
            'email': email,
            'address': address,
            'tel': tel,
            'picture': pic,
            'orderQS': orderQS,
            'deliverQS': deliverQS,
        }
    return render(request, "accounts/profile.html", context)


def settings(request):
    cus = get_object_or_404(Customer, email=request.user.email)
    online_cus = get_object_or_404(Online_Customer, tel_number=cus.tel_number)
    init = {
        'fname': cus.first_name,
        'lname': cus.last_name,
        'address': online_cus.address,
        'phone': online_cus.tel_number,
    }
    profile_form = EditProfile(initial=init)
    delete_form = deleteProfile()

    context = {
        'editform': profile_form,
        'deleteform': delete_form,
    }

    if request.method == "POST":
        if 'editform' in request.POST:
            profile_form = EditProfile(request.POST)
            if profile_form.is_valid():
                fname = profile_form.cleaned_data.get('fname')
                lname = profile_form.cleaned_data.get('lname')
                address = profile_form.cleaned_data.get('address')
                phone = profile_form.cleaned_data.get('phone')
                print(fname + ' ' + lname + ' ' + address)
                cus.first_name = fname
                cus.last_name = lname
                cus.tel_number = phone
                cus.save()
                online_cus.tel_number = phone
                online_cus.address = address
                online_cus.save()
        elif 'deleteform' in request.POST:
            delete_form = deleteProfile(request.POST)

            if delete_form.is_valid():
                password = delete_form.cleaned_data.get('password')
                print(password)
                user = authenticate(request, username=request.user.email, password=password)
                if user is not None:
                    # delete all tuples related to user
                    cus.delete()
                    online_cus.delete()
                    user.delete()
                    # logout
                else:
                    context = {
                        'editform': profile_form,
                        'deleteform': delete_form,
                        'error':'Invalid Password',
                    }
                    return render(request, "accounts/profile_settings.html", context)
        return redirect('/')


    return render(request, "accounts/profile_settings.html", context)


