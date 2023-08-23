from django.urls import path
from . import views

urlpatterns = [
    path('game/', views.blockrain_game, name='game'),
]
