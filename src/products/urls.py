from django.urls import path
# from . import views
from .views import *
from django.conf.urls import url



urlpatterns = [

    url(r'^list/$', Product_List_View),
    url(r'^ring_list/$', ring_list),

    # url(r'^list/(?P<pk>\d+)/$', Product_detail_View),

    url(r'^list/(?P<pk>\d+)/$', ProductDetailSlugView.as_view()),

    url(r'^list/(?P<slug>[\w-]+)/$', ProductDetailSlugView.as_view())

]