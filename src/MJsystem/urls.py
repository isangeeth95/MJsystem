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
from . import views

urlpatterns = [
    path('inventory/', include('inventory.urls')),
    path('order/', include('order.urls')),
    path('user/', include('accounts.urls')),
    path('delivery/', include('delivery.urls')),
    path('admin/', admin.site.urls),
    path('home/', views.home_page, name='home_page'),  # render index.html
    path('', views.index_page, name='index_page'),  # render index.html
    path('dashboard/', views.dashboard, name='dashboard'),
    path('test/', views.test_page, name='test'),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)