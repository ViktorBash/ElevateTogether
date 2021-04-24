from django.contrib import admin
from django.urls import path, include

from mysite.core import views


urlpatterns = [
    path('', views.home, name='home'),
    path('signup/', views.signup, name='signup'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('admin/', admin.site.urls),
    path("profile/<uuid:user_uuid>/", views.profile_view, name="profile_view"),
    path("profile_update/", views.profile_update, name="profile_update"),
]
