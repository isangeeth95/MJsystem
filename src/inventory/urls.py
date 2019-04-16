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

    url(r'^edit_items/(?P<pk>\d+)' , views.edit_items, name='edit_items'),
    url(r'^delete_items/(?P<pk>\d+)' , views.delete_items, name='delete_items'),

    url(r'^re_order$', views.re_order, name='re_order'),
    url(r'^add_Gold$', views.add_Gold, name='add_Gold'),
    url(r'^add_gold_submission$', views.add_gold_submission, name='add_gold_submission'),
    url(r'^rawMeterial$', views.rawMeterial, name='rawMeterial'),
    url(r'^gold$', views.Gold, name='gold'),
    url(r'^editGoldInfo/(?P<pk>\d+)', views.editGoldInfo, name='editGoldInfo'),
    url(r'^deleteGoldInfo/(?P<pk>\d+)', views.deleteGoldInfo, name='deleteGoldInfo'),
    url(r'^export/csv/$', views.export_Gold_csv, name='export_Gold_csv'),
    url(r'^export/xls/$', views.export_gold_xls, name='export_gold_xls'),
    url(r'^exportJewelry/csv/$', views.export_jewelry_csv, name='export_jewelry_csv'),

    url(r'^stone$', views.Stone, name='stone'),
    url(r'^add_stone$', views.add_stone, name='add_stone'),
    url(r'^edit_stone/(?P<pk>\d+)$', views.edit_stone, name='edit_stone'),
    url(r'^delete_stone_info/(?P<pk>\d+)$', views.delete_stone_info, name='delete_stone_info'),
    url(r'^export/csv/$', views.export_stone_csv, name='export_stone_csv'),

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