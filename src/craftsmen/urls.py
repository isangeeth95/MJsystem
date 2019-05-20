from django.urls import path
from .views import *
from django.conf.urls import url

urlpatterns = [
path('', craftsmenInfo, name ='craftsmenInfo'),
url(r'^add_craftsmen', add_craftsmen , name='add_craftsmen'),
url(r'^editcraftsmen/(?P<pk>\d+)', editcraftsmen, name='editcraftsmen'),
url(r'^delete_craftsmen/(?P<pk>\d+)', delete_craftsmen, name='delete_craftsmen'),
url(r'^exportcraftsmen/csv/$', export_craftsmen_csv, name='export_craftsmen_csv'),
url(r'^requested_jewelry', requestJewelry, name='requested_jewelry'),

]
