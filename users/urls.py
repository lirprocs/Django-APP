from django.urls import path
from . import views

urlpatterns = [
    path('login', views.login_in, name='login'),
    path('register', views.register, name='register'),
    path('logout', views.log_out, name='logout'),
]
