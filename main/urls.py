from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('support', views.support, name='support'),
    path('about', views.about, name='about'),
]
