from django.db import models
from django.db.models import Q
from users.models import CustomUser
from accommodation.models import Room as Reserved_room


class Reservation(models.Model):
    PENDING='Pending'
    CONFIRM='Confirm'
    CANCEL='Cancel'
    STATUS={
        PENDING:'Pending',
        CONFIRM:'Confirm',
        CANCEL:'Cancel',
    }
    check_in = models.DateField()
    check_out = models.DateField()
    nr_reservation = models.CharField(null=False)
    nr_person = models.IntegerField()
    nr_days=models.IntegerField(default=0)
    amount=models.FloatField(default=0.0)
    has_flights=models.BooleanField(default=True)
    status=models.CharField(choices=STATUS,default=PENDING)
    user = models.ForeignKey(CustomUser, on_delete = models.CASCADE)
    room = models.ForeignKey(Reserved_room, on_delete = models.CASCADE)
    
    def __str__(self):
        return self.nr_reservation
    

    def set_amount(self,newamount):
        if newamount > 0:
         self.amount=newamount
         self.save()
    def get_bookings_by_user(user):
       try:
        bookings=Reservation.objects.filter(user=user)
        return bookings
       except:
          print("An exception has occurred when selecting the booking")
  

    #  select the room that are not booked on the check_in, check_out dates
    def get_id_rooms_reserved(check_i, check_o):
       try:
         rooms_id= []
         rooms_id=Reservation.objects.filter(Q(check_in__range=(check_i,check_o))|
                                           Q(check_out__range=(check_i,check_o))|
                                           Q(check_in__lt=check_i,check_out__gt=check_o))

         return rooms_id
       except:
          print("An exception has occurred when selecting the rooms!")

    def cancel_booking(id):
       try:
          booking=Reservation.objects.get(id=id)
          print(booking)
          booking.status = 'Cancel'
          booking.save()
       except:
          print("ERORR CHANGHING STATUS BOOKING")
    def confirm_booking(id):
       try:
          booking=Reservation.objects.get(id=id)
          booking.status = booking.STATUS.CONFIRM
          booking.save()
       except:
          print("ERORR CHANGHING STATUS BOOKING")



