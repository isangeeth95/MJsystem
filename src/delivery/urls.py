from django.urls import path
from.import views
from django.conf.urls import url

urlpatterns = [
path('', views.deliveryInfo, name ='deliveryInfo'),
path('deliveryform/', views.add_deliveryform, name='add_delivery'),

url(r'^edit_delivery/(?P<pk>\d+)' , views.edit_deliveryform, name='edit_delivery'),
url(r'^delete_delivery/(?P<pk>\d+)' , views.delete_deliveryform, name='delete_delivery'),
]
