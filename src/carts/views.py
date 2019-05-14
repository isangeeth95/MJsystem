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
from delivery.forms import DeliveryAddressForm
from django.http.response import HttpResponse
import csv


# Create your views here.


def cart_detail_api_view(request):
    cart_obj, new_obj = Cart.objects.new_or_get(request)
    products = [{"name": x.category, "price": x.charges} for x in cart_obj.jewelries.all()]
    cart_data = {"subtotal": cart_obj.subtotal, "total": cart_obj.total, }
    return JsonResponse(cart_data)


def cart_home(request):
    cart_obj, new_obj = Cart.objects.new_or_get(request)
    # request.session['cart_number']
    print()
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
    delivery_address_form = DeliveryAddressForm()
    billing_address_id = request.session.get("billing_address_id", None)
    delivering_address_id = request.session.get("delivering_address_id", None)
    delivering_address = request.session.get("delivering_address")

    billing_profile, billing_profile_created = BillingProfile.objects.new_or_get(request)
    if billing_profile is not None:
        order_obj, order_obj_created = Order.objects.new_or_get(billing_profile, cart_obj)
        if delivering_address_id:
            order_obj.delivering_address = delivering_address
            del request.session["delivering_address_id"]
            order_obj.save()
        if billing_address_id:
            order_obj.billing_address = Address.objects.get(id=billing_address_id)
            del request.session["billing_address_id"]
        if billing_address_id or delivering_address_id:
            order_obj.save()

    if request.method == "POST":
        if order_obj.delivering_address:
            pass
        else:
            order_obj.assign_delivering_address_to_none()
        "Check that order is done"
        is_done = order_obj.check_done()
        if is_done:
            # TODO: decrease inventory
            # jewelry.objects.get().buy_item(value)
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
        "delivery_address_form": delivery_address_form,
    }
    return render(request, "order/checkout.html", context)


def checkout_done_view(request):
    return render(request, 'cart/checkout-done.html', {})


def cart_list_view(request):
    if request.user.is_admin or request.user.is_staff:
        print(request.user)
        cart_list = Cart.objects.all()
        context = {
            'cart_list': cart_list,
        }
    return render(request, "cart/admin-get-cart-list.html", context)


def export_cart_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="cart.csv"'

    writer = csv.writer(response)
    writer.writerow(['cartID', 'user', 'jewelries', 'subtotal', 'total', 'updated', 'timestamp'])
    cartInfo = Cart.objects.all().values_list('id', 'user', 'jewelries', 'subtotal', 'total', 'updated', 'timestamp')
    for info in cartInfo:
        writer.writerow(info)

    return response