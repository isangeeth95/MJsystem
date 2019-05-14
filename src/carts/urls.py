from django.urls import path
# from . import views
from .views import *
from django.conf.urls import url



urlpatterns = [

    url(r'^$', cart_home, name='home'),
    url(r'^update/$', cart_update, name='update'),
    url(r'^checkout/$', checkout_home, name='checkout'),
    url(r'^checkout/success/$', checkout_done_view, name='success'),
    url(r'^cart_list/$', cart_list_view, name='cart_list_view'),
]