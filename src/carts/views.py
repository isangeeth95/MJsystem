from django.shortcuts import render, redirect
from inventory.models import jewelry
from .models import Cart
from order.models import Order
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
    order_obj= None
    if cart_created or cart_obj.jewelries.count() == 0:
        return redirect("home")
    else:
        order_obj, new_order_obj= Order.objects.get_or_create(cart=cart_obj)
        return render(request, "order/checkout.html", {"object": order_obj})


