from django.urls import path
# from . import views
from .views import *
from django.conf.urls import url

urlpatterns = [
    # path('', views.user, name='blog-user'),
    path('login/', login_page, name='login-page'),
    path('logout/', log_out, name='logout-page'),
    path('signup/', signup, name='signup-page'),
    path('profile/', profile, name='profile-page'),
    path('settings/', settings, name='profile-settings-page'),
]