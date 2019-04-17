from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from django.http import Http404
from inventory.models import *
from carts.models import *


# Create your views here.


def Product_List_View(request):
    querySet = jewelry.objects.all()
    context = {
        'qs': querySet,
    }
    return render(request, "Products/product_list.html", context)


def ring_list(request):
    querySet = jewelry.objects.all()
    context = {
        'qs': querySet,
    }
    return render(request, "Products/ring_list.html", context)


# def Product_detail_View(self, pk=None, *args, **kwargs):
#     # instance = Ring.objects.get(id=pk)
#     instance = get_object_or_404(jewelry, id=pk)
#     request = self.request
#     cart_obj, new_obj = Cart.objects.new_or_get(request)
#     context = {
#         'object': instance,
#         'cart' : cart_obj,
#     }
#     return render(request, "Products/product_detail.html", context)


class ProductDetailSlugView(DetailView):
    queryset = jewelry.objects.all()
    template_name = "Products/product_detail.html"

    def get_context_data(self, *args, **kwargs):
        context = super(ProductDetailSlugView, self).get_context_data(*args, **kwargs)
        request = self.request
        cart_obj, new_obj = Cart.objects.new_or_get(request)
        context['cart'] = cart_obj
        return context

    def get_object(self, *args, **kwargs):
        request = self.request
        slug = self.kwargs.get('slug')
        try:
            instance = jewelry.objects.get(slug=slug)
        except jewelry.DoesNotExist:
            raise Http404("Not Found..")
        except jewelry.MultipleObjectsReturned:
            qs = jewelry.objects.filter(slug=slug)
            instance = qs.first()
        except:
            raise Http404("Errorrrr")
        return instance


def Product_detail_slug_View(request, pk=None, *args, **kwargs):
    # instance = Ring.objects.get(id=pk)
    instance = get_object_or_404(jewelry, id=pk)
    context = {
        'object': instance
    }
    return render(request, "Products/product_detail_slug.html", context)
