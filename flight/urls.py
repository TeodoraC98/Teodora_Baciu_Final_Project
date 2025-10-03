from django.urls import path, include
from . import views 
urlpatterns = [
 path('check_departure_flights/<str:type_flight>/',views.check_departure_flights, name='check_departure_flights'),
 path('get_return_flights/<int:index>/',views.get_return_flights, name='get_return_flights'),
 path('get_departure_flight/<int:index>/',views.get_departure_flight, name='departure_flight'),
 path('save_details_flight/',views.save_details_flight, name='save_details_flight'),
]