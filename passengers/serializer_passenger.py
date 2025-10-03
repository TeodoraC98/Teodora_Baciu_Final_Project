from rest_framework import serializers
from .models import Passenger
from flight.serializer_flights import ReservationFlightSerializer
class PassengerSerializer(serializers.ModelSerializer):
    reservation_flight=ReservationFlightSerializer(many=False, read_only=True)
    class Meta:
        model = Passenger
        fields = '__all__'
        
    def gey_passengers_list(reservation):
          list_passengers=[]
          passengers=Passenger.get_passengers_reservation(reservation)
          for passenger in passengers:
            sz_passenger=PassengerSerializer(passenger)
            list_passengers.append(sz_passenger.data)
          return list_passengers