from django.db import models
from users.models import CustomUser
from django.db.models import Q
from enum import Enum
class RoomType(models.Model):
    DELUXE='DELUXE'
    LUXURY='LUXURY'
    DOUBLE='DOUBLE'
    SINGLE='SINGLE'
    TYPES_ROOMS={
        DELUXE:"Deluxe",
        LUXURY:"Luxury",
        DOUBLE:"Double",
        SINGLE:"Single"
    }
    name = models.CharField(max_length=200)
    room_count = models.IntegerField()
    description = models.CharField(max_length=200)
    room_view =  models.CharField(max_length=100)
    type = models.CharField(choices=TYPES_ROOMS)
    def __str__(self):
        return self.type


class Room(models.Model):
    room_type = models.ForeignKey(RoomType, on_delete = models.CASCADE)
    description = models.CharField(max_length=200)
    price = models.IntegerField()
    room_number = models.IntegerField()
    room_capacity = models.PositiveIntegerField()

    def __str__(self):
        return str(self.room_number)
    
    def get_room_by_id(id):
        room = Room.objects.get(id=id)
        return room
    
    def set_price(self,new_price):
        if new_price >0:
            self.price=new_price
            self.save()
    
    def get_rooms_available(list_id,nr_pers):
       print(type(nr_pers))
       rooms=Room.objects.filter(~Q(id__in=list_id)).filter(room_capacity__gte=nr_pers)
       return rooms

class BenefitsPackage(models.Model):
        name=models.CharField(max_length=100)
        description=models.CharField(max_length=100)
        code=models.CharField(max_length=100,default="code")
        def __str__(self):
            return self.name
        
        @property
        def get_description(self):
            return self.description
        

class Package(models.Model):
    ALL_INCLUSICE='ALL INCLUSICE'
    FULL_BOARD='FULL BOARD'
    STANDARD='STANDARD'
    NAMES_PACKEGES={
    ALL_INCLUSICE:'All inclusive',
    FULL_BOARD:'Full board',
    STANDARD:'Standard'
    }
    room_type = models.ForeignKey(RoomType, on_delete = models.CASCADE)
    price=models.FloatField(default=0.0)
    name=models.CharField(choices=NAMES_PACKEGES,default=STANDARD)
    benefits=models.ManyToManyField(BenefitsPackage)
    def __str__(self):
        return self.name+' '+self.room_type.type

    def get_packages_room_type(room_type):
        packages_room_type= []
        packages_room_type=Package.objects.filter(Q(room_type=room_type))
        return packages_room_type
    
    @property
    def get_benefits(self):
         beneits=BenefitsPackage.objects.filter(package_id=self.id).values("description")
         return beneits
    @property
    def is_refundable(self):
        match self.name:
            case "ALL INCLUSICE":
                return True
            case "FULL BOARD":
                return True
            case _:
                return False
    



