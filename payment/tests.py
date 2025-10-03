from django.test import TestCase
from users.models import CustomUser
from bookings.models import Reservation
from accommodation.models import Room,RoomType
from .models import Payment
from datetime import datetime
# Create your tests here.
current_date=datetime.now().strftime('%Y-%m-%d')
class PaymentModelTests(TestCase):
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
   
    cls.payment =Payment.objects.create(
       amount=1000,
       date='2025-09-09',
       status='Pending',
       type='card',
        reservation =  cls.reservation
    )
 def test_payment_content(self):
      payment =Payment.objects.get(id=1)
      expect_amount = payment.amount
      expect_date = f'{payment.date }'
      expect_status = f'{payment.status }'
      expect_type= f'{payment.type }'
      expect_reservation= f'{payment.reservation }'
      self.assertEqual(expect_amount,1000),
      self.assertEqual(expect_date, current_date),
      self.assertEqual(expect_status ,"Pending"),
      self.assertEqual(expect_type,"card"),
      self.assertEqual(expect_reservation,"ejfncehvbeguy"),