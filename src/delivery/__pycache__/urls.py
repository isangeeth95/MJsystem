from django.urls import path
from.import views
from django.conf.urls import url

urlpatterns = [
#path('', views.deliveryInfo, name ='deliveryInfo'),
path('deliveryform/', views.add_deliveryform, name='add_delivery'),
path('deliprofile/', views.deliprofile, name='deliprofile-page'),
path('', views.staffdelivery, name='staffdelivery'),

url(r'^edit_delivery/(?P<pk>\d+)' , views.edit_deliveryform, name='edit_delivery'),
url(r'^staffedit_delivery/(?P<pk>\d+)' , views.staffedit_deliveryform, name='staffedit_delivery'),
url(r'^delete_delivery/(?P<pk>\d+)' , views.delete_deliveryform, name='delete_delivery'),
url(r'^export/csv/$', views.export_delivery_csv, name='export_delivery_csv'),
]
