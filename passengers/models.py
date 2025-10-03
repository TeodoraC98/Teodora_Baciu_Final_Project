from django.db import models
from flight.models import Reservation_Flight
# Create your models here.
class Passenger(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    nationality = models.CharField(max_length=150)
    date_of_birth = models.DateField()
    reservation_flight=models.ForeignKey(Reservation_Flight,on_delete = models.CASCADE)
    
    def __str__(self):
        return self.first_name
    
    def get_passengers_reservation(reservation_flight):
        try:
         passengers=Passenger.objects.filter(reservation_flight=reservation_flight)
         return passengers
        except:
           print("Error selecting the passenger")