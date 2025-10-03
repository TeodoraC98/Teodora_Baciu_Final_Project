from django.shortcuts import render,redirect
import requests
from bookings.views import context_flight, context_reservation_detail
from flight.models import Flight,DetailsRout,Reservation_Flight
from flight.serializer_flights import FlightSerializer
import string
import random
from dateutil import parser
from decouple import config
list_reservation_flights=[]
params={
      "api_key":config('API_KEY'),
      "engine":"google_flights",
      "arrival_id":"FNC"}
# Create your views here.
def nr_reservation_generator(size=10, chars=string.ascii_uppercase + string.digits):
 return ''.join(random.choice(chars) for _ in range(size))

def get_flights_details(params):
      search = requests.get("https://serpapi.com/search",params=params)
      response=search.json()
      if "best_flights" in  response:
       context_flight["best_flights"]=response["best_flights"]
      else:
       response["best_flights"]=0
      context_flight["other_flights"]=response["other_flights"]
     
def check_departure_flights(request,type_flight):
   params["departure_id"]=context_reservation_detail.get("departure_airport"),
   params["outbound_date"]=context_reservation_detail.get("booking").check_in,
   params["return_date"]=context_reservation_detail.get("booking").check_out,
   context_flight['type_flight']=type_flight
   if request.method=='GET':
       if "departure_token" in params:
        params.pop("departure_token")
       get_flights_details(params)
       context={
      "instances_flights":context_flight[type_flight],
        }
       return render(request,"flight/departure_flights.html",context=context)
     
   
def get_departure_flight(request,index):
      type_flight=context_flight.get('type_flight')
      obj_flight=context_flight[type_flight][index]
      params["departure_token"]=obj_flight['departure_token']
      save_details_flight(obj_flight)
      get_flights_details(params)
      context={
      "instances_flights":context_flight[type_flight]}
      return render(request,"flight/return_flights.html",context=context)




def get_return_flights(request,index):
      type_flight=context_flight.get('type_flight')
      obj_flight=context_flight[type_flight][index]
      save_details_flight(obj_flight)
      return redirect('info_passengers')
        



def save_details_flight(flight):
   reservation_flight=create_reservation_flight(
   context_reservation_detail.get("booking").nr_person,
   flight["price"])
   if reservation_flight:
    create_detail_flight(reservation_flight,flight)
   else:
      return False




def create_reservation_flight(nr_passangers,price):
   try:
    nr_reservation=nr_reservation_generator()
    reservation_flight=Reservation_Flight(nr_reservation=nr_reservation,
                                         nr_passengers=nr_passangers,
                                         price=price,
                                         reservation=context_reservation_detail.get("booking"))
    list_reservation_flights.append(reservation_flight)
    context_flight["reservation_flights"]=list_reservation_flights
    return reservation_flight
   except:
      print("An exception occurred")
      return False





def create_instance_flight(flight):
  try:
     instance_flight=Flight(departure_airport = flight["departure_airport"]["name"],
                             arrival_airport = flight["arrival_airport"]["name"],
                             flight_number = flight["flight_number"],
                             departure_date=parser.parse(flight["departure_airport"]["time"]),
                             arrival_date=parser.parse(flight["arrival_airport"]["time"]))
     return instance_flight

  except:
      print("An exception occurred")
      return False

def create_detail_flight(reservation_flight,obj_select_flight):
  try:

   list_objects_details_flight=[]
   for flight in obj_select_flight['flights']:
      instance_flight=create_instance_flight(flight)
      details_flight=DetailsRout(travel_class=flight["travel_class"],
                             airline=flight["airline"],
                             reservation_flight=reservation_flight,
                             flight=instance_flight)
      list_objects_details_flight.append(details_flight)
   context_flight[reservation_flight.nr_reservation]=list_objects_details_flight
  except:
      print("An exception occurred")
      return False


      

   