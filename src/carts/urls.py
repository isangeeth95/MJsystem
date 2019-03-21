from django.urls import path
# from . import views
from .views import *
from django.conf.urls import url



urlpatterns = [

    url(r'^$', cart_home, name='home'),
    url(r'^update/$', cart_update, name='update'),
]