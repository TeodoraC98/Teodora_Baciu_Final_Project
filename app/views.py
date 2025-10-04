from django.shortcuts import render
from bookings.models import Reservation
from flight.models import DetailsRout,Reservation_Flight,Flight                                                                          

def home(request):
    return render(request,"app/index.html")

def dashboard(request):
    bookings=Reservation.get_bookings_by_user(request.user)
    context={
        "bookings":bookings,
        }
    return render(request,"app/dashboard.html",context=context)
