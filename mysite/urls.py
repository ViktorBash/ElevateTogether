from django.contrib import admin
from django.urls import path, include

from mysite.core import views


urlpatterns = [
    path('', views.home, name='home'),
    path('signup/', views.signup, name='signup'),
    path('secret/', views.secret_page, name='secret'),
    path('secret2/', views.SecretPage.as_view(), name='secret2'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('admin/', admin.site.urls),
    path('wanting_to_learn/', views.users_wanting_learn, name="wanting_to_learn"),
    path('wanting_to_teach/', views.users_wanting_to_teach, name="wanting_to_teach"),
    path('skills_form/', views.fill_out_skills_form, name="skills_form"),
    path("profile/<uuid:user_uuid>/", views.profile_view, name="profile_view"),
]
