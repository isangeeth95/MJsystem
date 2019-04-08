from django.urls import path
from . import views
from .views import *
from django.conf.urls import url

urlpatterns = [
   # path('', views.hrmanage, name='blog-hrmanage'),
     path('', views.display_Trans, name='display_Trans'),
     path('add_Trans/', add_Trans, name='add_Trans' ),
     url(r'^edit_Trans/(?P<pk>\d+)' , views.edit_Trans, name='edit_Trans'),
     url(r'^delete_Trans/(?P<pk>\d+)' , views.delete_Trans, name='delete_Trans'),
     url(r'^exportBussinessAccounts/csv/$', views.export_BussinessAccounts_csv, name='export_BussinessAccounts_csv'),
]