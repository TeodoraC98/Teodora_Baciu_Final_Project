from django.contrib import admin
from .models import Flight,Reservation_Flight,DetailsRout
# Register your models here.
admin.site.register(Flight)
admin.site.register(DetailsRout)
admin.site.register(Reservation_Flight)