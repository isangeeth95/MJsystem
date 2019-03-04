from django.urls import path
from.import views
from .views import *
from django.conf.urls import url

urlpatterns = [
    path('',views.order, name ='blog-order'),
    #url(r'^display_order',)
]