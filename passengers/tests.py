from django.test import TestCase
from .models import Passenger
from users.models import CustomUser
from django.urls import reverse
from flight.models import Reservation_Flight
from bookings.models import Reservation
from accommodation.models import Room,RoomType
from .models import Passenger
class PassengerModelTests(TestCase):
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
    cls.reservation_flight=Reservation_Flight.objects.create(
      nr_passengers=4,
      nr_reservation='hdbscbfecxdec',
      price = 200,
      reservation=cls.reservation)
    cls.passenger =Passenger.objects.create(
        first_name = "first_name",
        last_name = "last_name",
        nationality = "nationality",
        date_of_birth ="2025-09-09",
        reservation_flight =  cls.reservation_flight
    )
 def test_passenger_content(self):
      passenger  = Passenger.objects.get(id=1)
      expect_first_name = f'{passenger.first_name}'
      expect_last_name = f'{passenger.last_name}'
      expect_nationality =f'{passenger.nationality}'
      expect_date_of_birth=f'{passenger.date_of_birth}'
      expect_reservation_flight=f'{passenger.reservation_flight}'
      self.assertEqual(expect_first_name,'first_name'),
      self.assertEqual(expect_last_name, "last_name"),
      self.assertEqual(expect_nationality ,"nationality"),
      self.assertEqual(expect_date_of_birth,"2025-09-09"),
      self.assertEqual(expect_reservation_flight,"hdbscbfecxdec"),

