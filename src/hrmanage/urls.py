from django.urls import path
from . import views
from .views import *
from django.conf.urls import url

urlpatterns = [
   # path('', views.hrmanage, name='blog-hrmanage'),
    path('', views.display_Staff, name='display_Staff'),
    path('add_Staff/', add_Staff, name='add_Staff' ),
    url(r'^edit_staff/(?P<pk>\d+)' , views.edit_staff, name='edit_staff'),
    url(r'^delete_staff/(?P<pk>\d+)' , views.delete_staff, name='delete_staff'),
    url(r'^exportStaff/csv/$', views.export_Staff_csv, name='export_Staff_csv'),

    # url(r'^add_Staff$', add_Staff, name='add_Staff'),
    #
    # url(r'^edit_Staff/(?P<pk>\d+)$', edit_Staff, name='edit_Staff'),
    #
    # url(r'^delete_Staff/(?P<pk>\d+)$', delete_Staff, name='delete_Staff'),
        ]