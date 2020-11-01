from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
app_name='home'
urlpatterns = [
    path('', views.HomeView.as_view(), name='all'),
    path('accounts/login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
]
