from django.urls import path
from . import views

urlpatterns = [
    path('process-code/', views.process_code, name='process_code'),
    path('take-test/<str:access_code>/', views.take_test, name='take_test'),
    path('code-display/<str:access_code>/', views.code_display, name='code_display'),
]
