from django.contrib import admin

# Register your models here.
from newbooking.models import Booking, Conveyance, Package, Price

admin.site.register(Booking)
admin.site.register(Conveyance)
admin.site.register(Package)
admin.site.register(Price)