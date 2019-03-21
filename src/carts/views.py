from django.shortcuts import render, redirect
from inventory.models import jewelry
from .models import Cart
# Create your views here.


def cart_home(request):
    cart_obj, new_obj = Cart.objects.new_or_get(request)
    return render(request, 'cart/home.html', {"cart": cart_obj})


def cart_update(request):
    jewelry_id = request.POST.get('jewelry_id')
    if jewelry_id is not None:
        try:
            jewelry_obj = jewelry.objects.get(id=jewelry_id)
        except jewelry.DoesNotExist:
            print("Show message to user, product is gone")
            return redirect('cart/home.html')
        cart_obj, new_obj = Cart.objects.new_or_get(request)
        if jewelry_obj in cart_obj.inventory.all():
            cart_obj.inventory.remove(jewelry_obj)
        else:
            cart_obj.inventory.add(jewelry_obj)
        request.session['cart_items'] = cart_obj.inventory.count()
    return redirect('cart/home.html')

