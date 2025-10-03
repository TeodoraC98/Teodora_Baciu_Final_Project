from django.test import TestCase
from .models import Room,RoomType

class RoomTypeModelTests(TestCase):
 @classmethod
 def setUpTestData(cls):
    cls.room_type=RoomType.objects.create(name ='name',
                                          room_count = 10,
                                          description = 'description',
                                         room_view ='room view',
                                         type='type') 
  
 def test_room_content(self):
   room_type  = RoomType.objects.get(id=1)
   expect_room_count =room_type.room_count
   expect_description = f'{ room_type.description}'
   expect_room_type_view =f'{room_type.room_view}'
   expect_room_type=f'{room_type.type}'
   self.assertEqual(expect_room_count,10),
   self.assertEqual(expect_description,'description'),
   self.assertEqual(expect_room_type_view,'room view'),
   self.assertEqual(expect_room_type,'type')

 def test_room_type_str_method(self):
    room_type = RoomType.objects.get(id=1)
    self.assertEqual(str(room_type), f'{room_type.type}')

class RoomModelTests(TestCase):
 @classmethod
 def setUpTestData(cls):
    cls.room_type=RoomType.objects.create(name ='name',room_count = 10,description = 'description', room_view ='room view',type='type') 
    cls.room=Room.objects.create(room_type =cls.room_type,
                                  description = "description",
                                  price =100,
                                  room_number = 101,
                                  room_capacity=2)   
 def test_room_content(self):
   room  = Room.objects.get(id=1)
   expect_room_type = f'{room.room_type}'
   expect_description = f'{room.description}'
   expect_price = room.price
   expect_room_number =room.room_number
   expect_room_capacity=room.room_capacity
   self.assertEqual(expect_room_type,'type'),
   self.assertEqual(expect_description,'description'),
   self.assertEqual(expect_price,100),
   self.assertEqual(expect_room_number,101)
   self.assertEqual(expect_room_capacity, 2)

 def test_room_str_method(self):
    room = Room.objects.get(id=1)
    self.assertEqual(str(room), f'{room.room_number}')

 def test_set_room_method(self):
       room = Room.objects.get(id=1)
       room.set_price(200)
       expecting_price=room.price
       self.assertEqual(200,expecting_price)  
 def test_get_room_method(self):
       room = Room.objects.get(id=1)
       get_room=Room.get_room_by_id(1)
       self.assertEqual(room,get_room)
