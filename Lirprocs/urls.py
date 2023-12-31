from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('register/', include('users.urls')),
    path('game/', include('game.urls')),
    path('user_profile/', include('user_profile.urls')),
    path('examination/', include('examination.urls')),
]
