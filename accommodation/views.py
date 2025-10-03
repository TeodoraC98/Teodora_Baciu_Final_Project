from django.shortcuts import render,redirect
from bookings.views import context_reservation_detail
from bookings.models import Reservation
from .models import RoomType,Room,Package,BenefitsPackage
from datetime import date
# Create your views here.

def check_availability_rooms(request):
      id_rooms_reserved=Reservation.get_id_rooms_reserved(
      context_reservation_detail.get("booking").check_in,
      context_reservation_detail.get("booking").check_out)
      av_rooms=Room.get_rooms_available(id_rooms_reserved,
                                       context_reservation_detail.get("booking").nr_person)
      context={
        "rooms":av_rooms,
        "booking":context_reservation_detail.get("booking")
       }
      return render(request,"accommodation/rooms_availability.html",context=context)


def details_room(request,id):
    if request.method =='POST':
      selected_package_id=request.POST.get("selected_package")
      context_reservation_detail["booking"].room_id=id
      if context_reservation_detail.get("is_package_with_flights"):
       return redirect('check_departure_flights',"other_flights")
      else:
        return redirect('payment')  
    else:
        room=Room.objects.get(id=id)
        packages=Package.get_packages_room_type(room.room_type)
        context={
         "room":room,
         "packages":packages,
         "booking":context_reservation_detail.get("booking"),
         "reservation":context_reservation_detail,
           }
        return render(request,"accommodation/details_room.html",context=context)
   


