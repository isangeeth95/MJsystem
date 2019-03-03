from django.urls import path
from.import views

urlpatterns = [
    path('login/', views.login_page, name='login-page'),
    path('logout/', views.log_out, name='logout-page'),
    path('signup/', views.signup, name='signup-page'),

]