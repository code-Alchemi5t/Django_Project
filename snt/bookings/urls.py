from django.urls import path
from . import views

app_name="bookings"
urlpatterns=[
    path('', views.Bookings.as_view(), name='all'),
    path('bookings/<int:pk>/update/', views.UpdateBookings.as_view(), name='booking_update'),
    path('bookings/<int:pk>/delete/', views.DeleteBookings.as_view(), name='booking_confirm_delete'),
]