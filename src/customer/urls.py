from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
        path('', views.customer_page, name ='customer-handling'),
        path('email/<str:email>', views.customer_mailing, name='customer-mail'),

        url(r'^info/(?P<pk>\d+)/$',views.customer_info, name='customer-info'),

]