from django.shortcuts import render,redirect
from django.conf import settings
from django.contrib.auth.decorators import login_required
from .models import Payment
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
@login_required
def get_payment_information(request):  
   if request.method=='GET':
      if context_reservation_detail.get("is_package_with_flights"):
         context={
         "booking":context_reservation_detail.get("booking"),
         "context_flight_details":get_objects_details_flight( get_keys_reservation_flights(context_flight.get("reservation_flights"))
                                    ,context_flight),
          "reservation_flights":context_flight.get("reservation_flights"),
          "passangers":context_reservation_detail.get("object_passengers"),
          "has_flights":context_reservation_detail.get("is_package_with_flights")}
         return  render(request,"payment/payment.html",context=context)
      else:
          context={
         "booking":context_reservation_detail.get("booking"),
         "has_flights":context_reservation_detail.get("is_package_with_flights")}
          return  render(request,"payment/payment.html",context=context)
   else:
    DOMAIN = f"{request.scheme}://{request.get_host()}"
    total=1000
  
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
        success_url=DOMAIN + f'/dashboard/',
        cancel_url=DOMAIN + f'/payment/cancel/',
    )
   payment=Payment(amount=total,
                   type=checkout_session.payment_method_types,
                   reservation=context_reservation_detail.get("booking"))
   confirm_info_reservation(request) 
   return redirect(checkout_session.url)


def success_payment(request):
    try:  
      return render(request,'dashboard')
    except Exception as e:
       print(e)



def cancel_payment(request):
     # update status  from pending to cancel
    try:
   
      return render(request,'payment/success.html')
    except Exception as e:
       print(e)

def insert_payment(amount):
   amount = amount
   type ='card'
   status ='pending'
   payment = Payment(amount,status,type)
   Payment.insert_payment_db(payment)
   return payment


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
      # set_total_amount_reservation(booking,reservation_flights)
   else:
      pass
      #  set_total_amount_reservation()
    
def confirm_info_reservation(request):
   save_booking_datails_bd(request.user)
   #   set_total_amount_reservation(booking,reservation_flight)
   
   

