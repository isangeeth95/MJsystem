from django.shortcuts import render, redirect
from inventory.models import jewelry
from .models import Cart
from order.models import Order
from billing.models import BillingProfile
from accounts.forms import LoginForm, GuestForm
from accounts.models import GuestEmail

# Create your views here.


def cart_home(request):
    cart_obj, new_obj = Cart.objects.new_or_get(request)
    return render(request, 'cart/home.html', {"cart": cart_obj})


def cart_update(request):
    product_id = request.POST.get('product_id')
    if product_id is not None:
        try:
            product_obj = jewelry.objects.get(id=product_id)
        except jewelry.DoesNotExist:
            print("Show message to user, product is gone")
            return redirect("home")
        cart_obj, new_obj = Cart.objects.new_or_get(request)
        if product_obj in cart_obj.jewelries.all():
            cart_obj.jewelries.remove(product_obj)
        else:
            cart_obj.jewelries.add(product_obj)
        request.session['cart_items'] = cart_obj.jewelries.count()
    return redirect("home")


def checkout_home(request):
    cart_obj, cart_created = Cart.objects.new_or_get(request)
    order_obj = None
    if cart_created or cart_obj.jewelries.count() == 0:
        return redirect("home")
    login_form = LoginForm()
    guest_form = GuestForm()

    billing_profile, billing_profile_created = BillingProfile.objects.new_or_get(request)
    if billing_profile is not None:
        order_obj, order_obj_created = Order.objects.new_or_get(billing_profile, cart_obj)

    context = {
        "object": order_obj,
        "billing_profile": billing_profile,
        "login_form": login_form,
        "guest_form": guest_form
    }
    return render(request, "order/checkout.html", context)


