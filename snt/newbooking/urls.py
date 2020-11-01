from django.urls import path, reverse_lazy
from . import views

app_name="newbooking"
urlpatterns=[
    path('', views.NewBookingCreate.as_view(), name='all'),
    path('newbooking/<int:pk>', views.ConfirmBooking.as_view(), name='confirm_booking'),
    path('newbooking/<int:pk>/delete', views.NewBookingDeleteView.as_view(success_url=reverse_lazy('newbooking:all')), name='newbooking_delete'),
]