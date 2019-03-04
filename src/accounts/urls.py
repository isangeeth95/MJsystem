from django.urls import path
from.import views
from .views import *
from django.conf.urls import url

urlpatterns = [
    path('', views.user, name='blog-user'),
    url(r'^login', login_page, name='login-page'),
    path('logout/', views.log_out, name='logout-page'),
    path('signup/', views.signup, name='signup-page'),
]