from django.urls import path
from . import views


urlpatterns = [
    path('profile', views.profile, name='profile'),
    path('redprofile/', views.redprofile, name='redprofile'),
    path('delete-account/', views.delete_account, name='delete_account'),
]