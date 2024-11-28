from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(User)
admin.site.register(UserVerification)
admin.site.register(Listing)
admin.site.register(Amenity)
admin.site.register(PropertyPhoto)
admin.site.register(Booking)
admin.site.register(Payment)
admin.site.register(Review)
admin.site.register(Message)
admin.site.register(Notification)
admin.site.register(SupportTicket)
admin.site.register(Blacklist)
admin.site.register(SecurityAlert)
admin.site.register(GeoTracking)
admin.site.register(Discount)
