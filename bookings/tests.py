from django.test import TestCase, Client
from users.models import CustomUser
from django.urls import reverse
from .models import Reservation
import datetime
from accommodation.models import Room,RoomType
# Create your tests here.
class ReservationModelTests(TestCase):
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
        nr_person = 2,
        nr_days=2,
        amount=400,
        user=cls.user, 
        room = cls.room)
    
 def test_reservation_content(self):
   reservation  = Reservation.objects.get(id=1)
   expect_check_in = f'{reservation.check_in}'
   expect_check_out = f'{reservation.check_out}'
   expect_nr_reservation = f'{reservation.nr_reservation}'
   expect_nr_person = reservation.nr_person
   expect_nr_days=reservation.nr_days
   expect_amount=reservation.amount
   expect_user=f'{reservation.user}'
   expect_room = f'{reservation.room}'
   self.assertEqual(expect_check_in,'2025-09-11'),
   self.assertEqual(expect_check_out,'2025-10-12'),
   self.assertEqual(expect_nr_reservation,'ejfncehvbeguy'),
   self.assertEqual(expect_nr_person,2)
   self.assertEqual(expect_nr_days, 2)
   self.assertEqual(expect_amount, 400)
   self.assertEqual(expect_user,'user@yahoo.com')
   self.assertEqual(expect_room, '101')

 def test_reservation_str_method(self):
    reservation = Reservation.objects.get(id=1)
    self.assertEqual(str(reservation), reservation.nr_reservation)

 def test_set_amount_method(self):
       reservation = Reservation.objects.get(id=1)
       reservation.set_amount(700)
       expecting_amount=reservation.amount
       self.assertEqual(700,expecting_amount)
    