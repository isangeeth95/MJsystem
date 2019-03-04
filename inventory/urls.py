from django.urls import path
from.import views 
from .views import *
from django.conf.urls import url

urlpatterns = [
path('',views.inventory, name ='blog-inventory'),
url(r'^display_Earrings$', display_Earrings, name='display_Earrings'),
url(r'^display_Necleces', display_Necleces, name='display_Necleces'),
url(r'^display_Ring', display_Ring, name='display_Ring'),
url(r'^display_Pendants', display_Pendants, name='display_Pendants'),

url(r'^add_Earrings$', add_Earrings, name='add_Earrings'),
url(r'^add_Necleces$', add_Necleces, name='add_Necleces'),
url(r'^add_Ring$', add_Ring, name='add_Ring'),
url(r'^add_Pendant$', add_Pendant, name='add_Pendant'),

url(r'^edit_Earrings/(?P<pk>\d+)$', edit_Earrings, name='edit_Earrings'),
url(r'^edit_Necleces/(?P<pk>\d+)$', edit_Necleces, name='edit_Necleces'),
url(r'^edit_Ring/(?P<pk>\d+)$', edit_Ring, name='edit_Ring'),
url(r'^edit_Pendant/(?P<pk>\d+)$', edit_Pendant, name='edit_Pendant'),

url(r'^delete_Earrings/(?P<pk>\d+)$', delete_Earrings, name='delete_Earrings'),
url(r'^delete_Necleces/(?P<pk>\d+)$', delete_Necleces, name='delete_Necleces'),
url(r'^delete_Ring/(?P<pk>\d+)$', delete_Ring, name='delete_Ring'),
url(r'^delete_Pendants/(?P<pk>\d+)$', delete_Pendants, name='delete_Pendants'),
]