from django.shortcuts import render
from newbooking.models import Booking
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from bookings.owner import OwnerUpdateView, OwnerDeleteView
from django.urls import reverse_lazy
from django.contrib.auth.models import User

class Bookings(LoginRequiredMixin, View):
    def get(self,request):
        booking_list=Booking.objects.filter(owner=self.request.user, status="Confirmed")
        ctx={'booking_list':booking_list}
        return render(request,'bookings/booking_list.html',ctx)
# Create your views here.

class UpdateBookings(OwnerUpdateView):
    model=Booking
    fields=['name','date','any_special_requests','preferred_mode_of_travel']
    template_name= 'bookings/booking_update_form.html'
    success_url=reverse_lazy('bookings:all')

class DeleteBookings(OwnerDeleteView):
    model=Booking
    template_name= 'bookings/booking_confirm_delete.html'
    success_url=reverse_lazy('bookings:all')

