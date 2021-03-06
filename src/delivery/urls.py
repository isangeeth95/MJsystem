from django.urls import path
from.import views
from django.conf.urls import url

urlpatterns = [
path('',views.mainstaffpage, name='mainstaffpage'),
path('deliveryInfo/', views.deliveryInfo, name ='deliveryInfo'),

path('deliprofile/', views.deliprofile, name='deliprofile-page'),
path('staffdelivery/', views.staffdelivery, name='staffdelivery'),
path('displayAreas/addarea/', views.addarea, name='addarea'),
path('displayAreas/', views.displayAreas, name='displayAreas'),
path('deliveryanalysis/', views.deliveryanalysis, name='deliveryanalyst'),

url(r'^edit_delivery/(?P<pk>\d+)' , views.edit_deliveryform, name='edit_delivery'),
url(r'^edit_deliveryArea/(?P<pk>\d+)' , views.edit_deliveryArea, name='edit_deliveryArea'),
url(r'^edit_deliveryhistory/(?P<pk>\d+)' , views.edit_deliveryhistory, name='edit_deliveryhistory'),
url(r'^staffedit_delivery/(?P<pk>\d+)' , views.staffedit_deliveryform, name='staffedit_delivery'),
url(r'^delete_delivery/(?P<pk>\d+)' , views.delete_deliveryform, name='delete_delivery'),
url(r'^delete_deliveryArea/(?P<pk>\d+)' , views.delete_deliveryArea, name='delete_deliveryArea'),
url(r'^export/csv/$', views.export_delivery_csv, name='export_delivery_csv'),
]
