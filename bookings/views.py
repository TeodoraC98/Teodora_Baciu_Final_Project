from django.shortcuts import render,redirect
from .models import Reservation
from flight.models import Reservation_Flight,DetailsRout,Flight
from flight.serializer_flights import DetailsRoutSerializer
from accommodation.models import RoomType,Room
from django.contrib.auth.decorators import login_required
from passengers.models import Passenger
from passengers.serializer_passenger import PassengerSerializer
from datetime import datetime
import string
import random
date_format = "%Y-%m-%d"
from bookings.departure_airports import departure_airports
list_airports={
"departure_airports":departure_airports,
}
context_flight={

}
context_reservation_detail={

}
def nr_reservation_generator(size=30, chars=string.ascii_uppercase + string.digits):
 return ''.join(random.choice(chars) for _ in range(size))


def reservation_number_of_days(check_in,check_out):
    day_out = datetime.strptime(check_out,date_format)
    day_in= datetime.strptime(check_in,date_format)
    nr_days=day_out-day_in
    return nr_days.days



@login_required
def strat_reservation(request):
    if request.method=='POST':
     check_in=request.POST.get("availability_room-check-in")
     check_out=request.POST.get("availability_room-check-out")
     has_flights=eval(request.POST.get("btnradio"))
     departure_airport=request.POST.get("select_departure_airport")
     nr_persons=int(request.POST.get("nr_pers"))
     nr_days=reservation_number_of_days(check_in,check_out)
     reservation=Reservation(check_in=check_in,
                             check_out=check_out,
                             nr_reservation=nr_reservation_generator(),
                             nr_person=nr_persons,
                             nr_days=nr_days,
                             has_flights=has_flights)
     context_reservation_detail["booking"]=reservation
     context_reservation_detail["departure_airport"]= departure_airport
     context_reservation_detail["is_package_with_flights"]=has_flights
     
     return redirect('check_availability_rooms')
    return render(request,"bookings/reservation_information.html",context=list_airports)


def dictionary_details_flight(reservation_flights):
    dict_flights={}
    
    for reservation_flight in reservation_flights:
       list_df=[]
       detail_flight=DetailsRout.get_detail_flights_reservation(reservation_flight)
       for dt in detail_flight:
           sz_detail=DetailsRoutSerializer(dt)
           list_df.append(sz_detail)
       dict_flights[reservation_flight.nr_reservation]=list_df
    return dict_flights


def get_details_booking(request,id):
    booking=Reservation.objects.get(id=id)
    if request.method=='GET':
        if booking.has_flights:
         reservation_flights=Reservation_Flight.get_reservation_by_booking_id(booking)
         context={
           "booking":booking,
           "context_flight_details":dictionary_details_flight(reservation_flights),
           "reservation_flights":reservation_flights,
           "passangers":PassengerSerializer.gey_passengers_list(reservation_flights[0]),
          }
        else:context={
           "booking":booking}
        return  render(request,"bookings/details_booking.html",context=context)
    else:
       pass

def cancel_booking(request,id):
   Reservation.cancel_booking(id)
   return redirect('details_booking',id)

def delete_booking(request,id):
   print("delete")
   return redirect('dashboard')
       
       

