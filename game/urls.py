from django.urls import path
from . import views

urlpatterns = [
    path('game/', views.tic_tac_toe_view, name='game'),
]
