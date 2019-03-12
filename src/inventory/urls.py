from django.urls import path
from.import views 
from .views import *
from django.conf.urls import url

urlpatterns = [
    path('', views.inventory, name='blog-inventory'),
    url(r'^add_Item', add_Item, name='add_Item'),
    url(r'^display_Earrings$', display_Earrings, name='display_Earrings'),
    url(r'^display_Necklaces$', display_Necklaces, name='display_Necklaces'),
    url(r'^display_Ring$', display_Ring, name='display_Ring'),
    url(r'^display_Pendants$', display_Pendants, name='display_Pendants'),

#
# url(r'^edit_Earrings/(?P<pk>\d+)$', edit_Earrings, name='edit_Earrings'),
# url(r'^edit_Necklaces/(?P<pk>\d+)$', edit_Necklaces, name='edit_Necklaces'),
# url(r'^edit_Ring/(?P<pk>\d+)$', edit_Ring, name='edit_Ring'),
# url(r'^edit_Pendant/(?P<pk>\d+)$', edit_Pendant, name='edit_Pendant'),
#
# url(r'^delete_Earrings/(?P<pk>\d+)$', delete_Earrings, name='delete_Earrings'),
# url(r'^delete_Necklaces/(?P<pk>\d+)$', delete_Necklaces, name='delete_Necklaces'),
# url(r'^delete_Ring/(?P<pk>\d+)$', delete_Ring, name='delete_Ring'),
# url(r'^delete_Pendants/(?P<pk>\d+)$', delete_Pendants, name='delete_Pendants'),
]