from django.urls import path
from . import views
# from django.contrib.auth import views as auth_views
app_name = 'user'
urlpatterns = [
    path('', views.SignUp.as_view(), name='all'),
]
