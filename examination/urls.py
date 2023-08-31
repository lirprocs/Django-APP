from django.urls import path
from . import views

urlpatterns = [
    path('process-code/', views.process_code, name='process_code'),
    path('enter-code/', views.enter_code, name='enter_code'),
    path('take-test/<str:access_code>/', views.take_test, name='take_test'),
    path('test-results/', views.test_results, name='test_results'),
    path('code-display/<str:access_code>/', views.code_display, name='code_display'),
]
