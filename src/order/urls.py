from django.urls import path
from.import views
from .views import *
from django.conf.urls import url

urlpatterns = [
    path('',views.order, name ='blog-order'),
    url(r'^order_list/$', order_list_view, name='order_list_view'),
    #url(r'^display_order',)
]