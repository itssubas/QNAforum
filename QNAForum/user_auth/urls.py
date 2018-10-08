from django.urls import path, re_path
from user_auth import views as user_views
from django.contrib.auth import views as auth_views



urlpatterns = [
    re_path(r'^register/', user_views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('profile/', user_views.profile, name='profile'),
]
