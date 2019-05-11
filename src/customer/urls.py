from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
        path('', views.customer_page, name ='customer-handling'),

        url(r'^info/(?P<pk>\d+)/$',views.customer_info, name='customer-info'),

]