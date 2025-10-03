from django.shortcuts import render
from bookings.models import Reservation
from flight.models import DetailsRout,Reservation_Flight,Flight

# def dictionary_details_flight(reservation_flights):
#     dict_flights={    }
#     for reservation_flight in reservation_flights:
#        detail_flight=DetailsRout.get_detail_flights_reservation(reservation_flight)
#        print(detail_flight)
#        dict_flights[reservation_flight.reservation]=detail_flight
#     print(dict_flights)
#     return dict_flights
# def dictionary_reservation_flights(bookings):
#     dict_reservation_flights={    }
#     for booking in bookings:
#        reservation_flights=Reservation_Flight.get_reservation_by_booking_id(booking)
#        print(reservation_flights)
#        dict_reservation_flights["reservation_flight"]=reservation_flights
#        for reservation_flight in reservation_flights:
#          details_flight=DetailsRout.get_detail_flights_reservation(reservation_flight)
#          dict_reservation_flights["details_fligt"]=details_flight
#     print(dict_reservation_flights)
#     return dict_reservation_flights
# def dictionary_booking_details(bookings):
#     dict_bookind_info={}
#     for booking in bookings:
#         dict_bookind_info[booking.nr_reservation]["booking"]=booking
#         dict_bookind_info[booking.nr_reservation]["reservation_flights"]=Reservation_Flight.get_reservation_by_booking_id(booking)
                                                                                                                          

def home(request):
    return render(request,"app/index.html")

def dashboard(request):
    bookings=Reservation.get_bookings_by_user(request.user)

    # flights=dictionary_reservation_flights(bookings)
    # details_flights=dictionary_details_flight()
    context={
        "bookings":bookings,
        # "context_flights":dictionary_reservation_flights(bookings),
        # "reservation_flights":reservation_flights,
        # "passangers":.get("object_passengers"),
        # "has_flights":context_reservation_detail.get("is_package_with_flights")
        }
    return render(request,"app/dashboard.html",context=context)
