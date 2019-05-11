"""MJsystem URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from . import views
from addresses.views import checkout_address_create_view
from carts.views import cart_detail_api_view
from delivery.views import checkout_delivery_address_create_view


urlpatterns = [
                  path('inventory/', include('inventory.urls')),
                  path('order/', include('order.urls')),
                  path('products/', include('products.urls')),
                  path('cart/', include('carts.urls')),
                  url(r'^checkout/address/create/$', checkout_address_create_view, name='checkout_address_create'),
                  url(r'^checkout/delivery/address/create/$', checkout_delivery_address_create_view, name='checkout_delivery_address_create'),
                  url(r'^api/cart/$', cart_detail_api_view, name='api-cart'),
                  path('dashboard/customer/', include('customer.urls')),
                  path('user/', include('accounts.urls')),
                  path('delivery/', include('delivery.urls')),
                  path('admin/', admin.site.urls),
                  path('home/', views.index_page, name='index_page'),  # render index.html
                  # path('', views.home_page, name='home_page'),  # render index.html
                  path('', views.index_page, name='index_page'),  # render index.html
                  path('dashboard/', views.dashboard, name='dashboard'),
                  path('contact/', views.contact_page, name='contact_page'),  # render index.html
                  path('about/', views.about_page, name='about_page'),
                  path('test/', views.test_page, name='test'),
                  path('hrmanage/', include('hrmanage.urls')),
                  path('supplier/', include('supplier.urls')),
                  path('craftsmen/', include('craftsmen.urls')),
                  path('BussinessAccounts/', include('BussinessAccounts.urls')),
                  path('accounts/', include('accounts.password.urls')), # for password reset
              ]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

