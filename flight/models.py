from django.db import models
from django.utils import timezone
from bookings.models import Reservation
# Create your models here.

    


class Reservation_Flight(models.Model):
    nr_reservation=models.CharField(max_length=100)
    nr_passengers=models.IntegerField()
    price = models.FloatField(default=0.0)
    reservation=models.ForeignKey(Reservation,on_delete=models.CASCADE,null=True,blank=True)
    def __str__(self):
        return str(self.nr_reservation)
    
    def set_price(self,price):
        self.price =self.price+price
    
    def get_reservation_by_booking_id(bookingId):
        reservation_flighs = Reservation_Flight.objects.filter(reservation=bookingId)
        return reservation_flighs
  
class Flight(models.Model):
    departure_airport = models.CharField(max_length=200)
    arrival_airport = models.CharField(max_length=200)
    flight_number=models.CharField(max_length=20)
    departure_date=models.DateField(blank=True,null=True)
    arrival_date=models.DateField(blank=True,null=True)
    create_on=models.DateField(auto_now_add=True,blank=True,null=True)
    def __str__(self):
        return self.flight_number
    
class DetailsRout(models.Model):
    travel_class=models.CharField(max_length=200,blank=True)
    airline=models.CharField(max_length=200,blank=True)
    reservation_flight=models.ForeignKey(Reservation_Flight,on_delete=models.CASCADE,null=True,blank=True)  
    flight=models.ForeignKey(Flight,on_delete=models.CASCADE,null=False)

    def __str__(self):
        return str(self.airline)
    # def get_flights_by_id_rout(id):
    #      flights= []
    #      flights=Reservation.objects.filter(Q(check_in__range=(check_i,check_o))|
    #                                        Q(check_out__range=(check_i,check_o))|
    #                                        Q(check_in__lt=check_i,check_out__gt=check_o))
    def get_detail_flights_reservation(reservation_flight):
        try:
            details_flights=DetailsRout.objects.filter(reservation_flight=reservation_flight)
            return details_flights
        except:
            print("An exception has occurred when selectinf details flights")
    @property
    def get_flight(self):
        details_rout=DetailsRout.objects.get(id=self.id)
        return details_rout