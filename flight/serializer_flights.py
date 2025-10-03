from rest_framework import serializers
from .models import Flight, DetailsRout,Reservation_Flight

class ReservationFlightSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation_Flight
        fields = '__all__'


class FlightSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flight
        fields = "__all__"

class DetailsRoutSerializer(serializers.ModelSerializer):
    reservation_flight=ReservationFlightSerializer(many=False, read_only=True)
    flight=FlightSerializer(many=False, read_only=True)
    class Meta:
        model = DetailsRout
        fields = ['id','travel_class','airline','reservation_flight', 'flight']