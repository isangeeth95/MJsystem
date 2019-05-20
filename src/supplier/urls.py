from django.urls import path
from .views import *
from django.conf.urls import url

urlpatterns = [
path('', supplierInfo, name ='supplierInfo'),
url(r'^add_supplier$', add_supplier , name='add_supplier'),
url(r'^edit_supplier/(?P<pk>\d+)', edit_supplier, name='edit_supplier'),
url(r'^delete_Sup/(?P<pk>\d+)', delete_Sup, name='delete_Sup'),
url(r'^exportsupplier/csv/$', export_supplier_csv, name='export_supplier_csv'),

]
