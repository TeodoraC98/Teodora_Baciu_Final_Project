from django.shortcuts import render,redirect
from django.conf import settings
from django.contrib.auth.decorators import login_required
from .models import Payment
from bookings.models import Reservation
import stripe
stripe.api_key = settings.STRIPE_SECRET_KEY
from bookings.views import context_reservation_detail,context_flight
# Create your views here.
import os

def get_objects_details_flight(keys,context):
   objects_details_flight=[]
   for key in keys:
      objects_details_flight.append(context.get(key))
   return objects_details_flight

def get_keys_reservation_flights(reservation_flights):
   keys=[]
   for reservtion in reservation_flights:
      keys.append(reservtion.nr_reservation)
   return keys
def set_total_booking(booking,resevation_flights):
     for reservation_fl in resevation_flights:
       booking.amount=booking.amount+reservation_fl.price
    
  

def save_object_db_flights(reservations_flight):
    for reservation in reservations_flight:
      for details_flight in context_flight.get(reservation.nr_reservation):
         flight=details_flight.flight
         flight.save()
         details_flight.save()
      

def save_object_db_passengers(list_passengers,booking):
   for reservation_flight in booking:
    for passanger in list_passengers:
       passanger.reservation_flight=reservation_flight
       passanger.save()
       
def save_reservations_flights_db(reservations):
   for reservation in reservations:
      reservation.save()

def set_total_amount_reservation(booking_ref,flight_ref):
   if booking_ref & flight_ref:
      total=booking_ref.room.price*booking_ref.nr_days
      total=total+flight_ref.price
 
def save_booking_datails_bd(user):
   booking=context_reservation_detail.get("booking")
   booking.user=user
   booking.save()
   if  context_reservation_detail.get("is_package_with_flights"):
    reservation_flights=context_flight.get("reservation_flights")
    save_reservations_flights_db( reservation_flights)
    list_passangers=context_reservation_detail.get("object_passengers")
    save_object_db_passengers(list_passangers,reservation_flights)
    save_object_db_flights( reservation_flights) 
   
   
def save_payment_db(reservation,amount,type):
   try:
    Payment.objects.create(amount=amount,
                   type=type,
                   reservation=reservation)
   except:
      print("Error saving payment in database")
   

    
@login_required
def get_payment_information(request):  
   booking=context_reservation_detail.get("booking")
   if request.method=='GET':
      if context_reservation_detail.get("is_package_with_flights"):
         flight_details=get_objects_details_flight( get_keys_reservation_flights(context_flight.get("reservation_flights"))
                                    ,context_flight)
         reservation_flights=context_flight.get("reservation_flights")
         passangers=context_reservation_detail.get("object_passengers")
         set_total_booking(booking,reservation_flights)
         context={
         "booking":booking,
         "context_flight_details":flight_details,
          "reservation_flights":reservation_flights,
          "passangers":passangers,
          "has_flights":context_reservation_detail.get("is_package_with_flights")}
         return  render(request,"payment/payment.html",context=context)
      else:
          context={
         "booking":context_reservation_detail.get("booking"),
         "has_flights":context_reservation_detail.get("is_package_with_flights")}
          return  render(request,"payment/payment.html",context=context)
   else:
    DOMAIN = f"{request.scheme}://{request.get_host()}"
    total=int(booking.amount*100)
  
    checkout_session = stripe.checkout.Session.create(
        line_items=[
            {
           
                'price_data': {
                    'product_data': {
                        'name': 'Mala Hotel',
                    },
                    'unit_amount': total ,
                    'currency': 'eur',
                },
                'quantity': 1,
            },
        ],
        payment_method_types=['card'],
        mode='payment',
        success_url=DOMAIN + f'/payment/success_payment/',
        cancel_url=DOMAIN + f'/payment/cancel_payment/',
    )
   save_booking_datails_bd(request.user)
   save_payment_db(booking,total, checkout_session.payment_method_types) 
   return redirect(checkout_session.url,id)


def success_payment(request):
     # update status  from pending to paid
   if request.method=='GET':
    try:  
       booking=context_reservation_detail.get("booking")
       Reservation.confirm_bookin_nr_reservation(booking.nr_reservation)
       Payment.set_payment_paid(booking)
    except Exception as e:
       print(e)
    return render(request,'payment/success.html')


def cancel_payment(request):
     # update status  from pending to cancel
   if request.method=='GET':
    try:
      booking=context_reservation_detail.get("booking")
      Reservation.cancel_booking_nr_reservation(booking.nr_reservation)
      Payment.set_payment_cancel(booking)
    except Exception as e:
       print(e)
   return render(request,'payment/cancel.html')

