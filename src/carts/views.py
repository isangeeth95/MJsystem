from django.http import JsonResponse
from django.shortcuts import render, redirect
from inventory.models import jewelry
from .models import Cart
from order.models import Order
from billing.models import BillingProfile
from addresses.models import Address
from accounts.forms import LoginForm, GuestForm
from accounts.models import GuestEmail
from addresses.forms import AddressForm

# Create your views here.


def cart_detail_api_view(request):
    cart_obj, new_obj = Cart.objects.new_or_get(request)
    products = [{"name": x.category, "price": x.charges} for x in cart_obj.jewelries.all()]
    cart_data = {"subtotal": cart_obj.subtotal, "total": cart_obj.total, }
    return JsonResponse(cart_data)


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
            added = False
        else:
            cart_obj.jewelries.add(product_obj)
            added = True
        request.session['cart_items'] = cart_obj.jewelries.count()
        if request.is_ajax():#Asynchronus javascript and xml / json
            print("Ajax request")
            json_data = {
                "added": added,
                "removed": not added,
                "cartItemCount": cart_obj.jewelries.count(),
            }
            return JsonResponse(json_data)
    return redirect("home")







def checkout_home(request):
    cart_obj, cart_created = Cart.objects.new_or_get(request)
    order_obj = None
    if cart_created or cart_obj.jewelries.count() == 0:
        return redirect("home")
    login_form = LoginForm()
    guest_form = GuestForm()
    address_form = AddressForm()
    billing_address_id = request.session.get("billing_address_id", None)
    # delivering_address_id = request.session.get("delivering_address_id", None)

    billing_profile, billing_profile_created = BillingProfile.objects.new_or_get(request)
    if billing_profile is not None:
        order_obj, order_obj_created = Order.objects.new_or_get(billing_profile, cart_obj)
        # if delivering_address_id:
        #     order_obj.delivering_address = Address.objects.get(id=delivering_address_id)
        #     del request.session["delivering_address_id"]
        if billing_address_id:
            order_obj.billing_address = Address.objects.get(id=billing_address_id)
            del request.session["billing_address_id"]
        # if billing_address_id or delivering_address_id:
        if billing_address_id:
            order_obj.save()

    if request.method == "POST":
        "Check that order is done"
        is_done = order_obj.check_done()
        if is_done:
            order_obj.mark_paid()
            request.session['cart_items'] = 0
            del request.session['cart_id']
            print(request.session.get("cart_items"))
            return redirect("success")
        else:
            print("is done is returning False")

    context = {
        "object": order_obj,
        "billing_profile": billing_profile,
        "login_form": login_form,
        "guest_form": guest_form,
        "address_form": address_form,
    }
    return render(request, "order/checkout.html", context)


def checkout_done_view(request):
    return render(request, 'cart/checkout-done.html', {})

