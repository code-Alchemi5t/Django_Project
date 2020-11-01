from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from newbooking.owner import OwnerDeleteView, OwnerUpdateView
from django.urls import reverse
from newbooking.forms import CreateForm
from newbooking.models import Booking, Price
from django.shortcuts import render, redirect


class NewBookingDeleteView(OwnerDeleteView):
    model = Booking
    success_url='newbooking:all'


class NewBookingCreate(LoginRequiredMixin, View):
    template_name='newbooking/booking_form.html'
    success_url='newbooking:all'
    def get(self,request,pk=None):
        form=CreateForm()
        ctx={'form':form}
        return render(request,self.template_name,ctx)

    def post(self,request,pk=None):
        form=CreateForm(request.POST)
        if not form.is_valid():
            ctx={'form':form}
            return render(request,self.template_name,ctx)

        booking=form.save(commit=False)
        booking.owner=self.request.user
        booking.save()
        return redirect(reverse('newbooking:confirm_booking', args=[booking.id]))

class ConfirmBooking(LoginRequiredMixin, View):
    def get(self,request,pk):
        booking=Booking.objects.get(id=pk)
        y=Price.objects.get(destination=booking.package)
        x=booking.no_of_People
        z=y.cost
        z=z*x
        ctx={'booking':booking,'cost':z}
        return render(request,'newbooking/confirm_booking.html',ctx)

    def post(self,request,pk):
        booking=Booking.objects.get(id=pk)
        booking.status='Confirmed'
        booking.save()
        return redirect('home:all')


