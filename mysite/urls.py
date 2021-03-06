from django.contrib import admin
from django.urls import path, include

from mysite.core import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('', views.learn, name='learn'),
    path('signup/', views.signup, name='signup'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('admin/', admin.site.urls),
    path("profile/<uuid:user_uuid>/", views.profile_view, name="profile_view"),
    path("profile_update/", views.profile_update, name="profile_update"),
    path('', include('chat.urls'))
]

urlpatterns += staticfiles_urlpatterns()