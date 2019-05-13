from django.urls import path
from.import views
from .views import *
from django.conf.urls import url

urlpatterns = [
    path('',views.admin_view_orders, name ='admin_view_orders'),
    url(r'^order_list/$', order_list_view, name='order_list_view'),
    url(r'^order_list/dashboard/$', admin_view_orders, name='admin_view_orders'),
    url(r'^created/$', created_order_view, name='created_order_view'),
    #url(r'^display_order',)admin_view_orders
]