from django.test import TestCase
from .models import Reservation_Flight,Flight,DetailsRout
from bookings.models import Reservation
from users.models import CustomUser
from accommodation.models import Room,RoomType
from datetime import datetime
# Create your tests here.
current_date=datetime.now().strftime('%Y-%m-%d')
class ReservationFlightModelTests(TestCase):
 @classmethod
 def setUpTestData(cls):
    cls.room_type=RoomType.objects.create(name ='name',room_count = 10,description = 'description', room_view ='room view',type='type') 
    cls.user = CustomUser.objects.create_user(username='user',email='user@yahoo.com', password='password')
    cls.room=Room.objects.create(room_type = cls.room_type,
                                  description = "description",
                                  price =100,
                                  room_number = 101,
                                  room_capacity=2)   
    cls.reservation=Reservation.objects.create(
        check_in = '2025-09-11',
        check_out = '2025-10-12',
        nr_reservation ='ejfncehvbeguy',
        nr_person = 4,
        nr_days=2,
        amount=400,
        user=cls.user, 
        room = cls.room)
    cls.reservation_flight=Reservation_Flight.objects.create(
      nr_passengers=4,
      nr_reservation='hdbscbfecxdec',
      price = 200,
      reservation=cls.reservation)
  
 def test_reservation_flight_content(self):
   reservation_flight  = Reservation_Flight.objects.get(id=1)
   expect_nr_passengers =reservation_flight.nr_passengers
   expect_nr_reservation = f'{ reservation_flight.nr_reservation}'
   expect_price =reservation_flight .price
   expect_reservation=f'{reservation_flight.reservation}'
   self.assertEqual(expect_nr_passengers,4),
   self.assertEqual(expect_reservation,"ejfncehvbeguy"),
   self.assertEqual(expect_price,200),
   self.assertEqual(expect_nr_reservation,'hdbscbfecxdec')

class FlightModelTests(TestCase):
 @classmethod
 def setUpTestData(cls):
    cls.flight =Flight.objects.create(
    departure_airport = "departure_airport",
    arrival_airport = "arrival_airport",
    flight_number="ffwRFr",
    departure_date="2025-09-16",
    arrival_date="2025-09-16"),
 def test_flight_content(self):
   flight  = Flight.objects.get(id=1)
   expect_departure_airport =f'{flight.departure_airport}'
   expect_arrival_airport = f'{flight.arrival_airport}'
   expect_flight_number =f'{flight.flight_number}'
   expect_departure_date=f'{flight.departure_date}'
   expect_arrival_date=f'{flight.arrival_date}'
   expect_create_on=f'{flight.create_on}'
   self.assertEqual(expect_departure_airport,'departure_airport'),
   self.assertEqual(expect_arrival_airport, "arrival_airport"),
   self.assertEqual(expect_flight_number ,"ffwRFr"),
   self.assertEqual(expect_departure_date,"2025-09-16"),
   self.assertEqual(expect_arrival_date ,"2025-09-16"),
   self.assertEqual(expect_create_on , current_date),

class DetailsRoutModelTests(TestCase):
 @classmethod
 def setUpTestData(cls):
    cls.room_type=RoomType.objects.create(name ='name',room_count = 10,description = 'description', room_view ='room view',type='type')
    cls.user = CustomUser.objects.create_user(username='user',email='user@yahoo.com', password='password')
    cls.room=Room.objects.create(room_type =cls.room_type,
                                  description = "description",
                                  price =100,
                                  room_number = 101,
                                  room_capacity=2)
    cls.reservation=Reservation.objects.create(
        check_in = '2025-09-11',
        check_out = '2025-10-12',
        nr_reservation ='ejfncehvbeguy',
        nr_person = 4,
        nr_days=2,
        amount=400,
        user=cls.user, 
        room = cls.room)
    cls.flight = Flight.objects.create(
       departure_airport = "departure_airport",
       arrival_airport = "arrival_airport",
       flight_number="ffwRFr",
       departure_date="2025-09-16",
       arrival_date="2025-09-16")
    cls.reservation_flight=Reservation_Flight.objects.create(
      nr_passengers=4,
      nr_reservation='hdbscbfecxdec',
      price = 200,
      reservation=cls.reservation)
    cls.details_flight=DetailsRout.objects.create(
       travel_class="travel_class",
       airline="airline",
       reservation_flight=cls.reservation_flight,
       flight=cls.flight
      )
 def test_details_flight_content(self):
      details_flight  = DetailsRout.objects.get(id=1)
      expect_travel_class = f'{details_flight.travel_class}'
      expect_airline = f'{details_flight.airline}'
      expect_reservation_flight =f'{details_flight.reservation_flight}'
      expect_flight=f'{details_flight.flight}'
      self.assertEqual(expect_travel_class,'travel_class'),
      self.assertEqual(expect_airline, "airline"),
      self.assertEqual(expect_reservation_flight ,"hdbscbfecxdec"),
      self.assertEqual(expect_flight,"ffwRFr"),