from django.contrib import admin
from django.urls import path, include
from . import views 
urlpatterns = [
    path('check_availability_rooms',views.check_availability_rooms,name='check_availability_rooms'),
    path('details_room/<int:id>/',views.details_room, name='details_room'),
    # path('confirm_room_accommodation/<int:id>/',views.confirm_room_accommodation, name='confirm_room_accommodation'),
]
