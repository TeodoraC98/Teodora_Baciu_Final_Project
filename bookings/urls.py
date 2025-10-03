
from django.urls import path
from . import views 
urlpatterns = [
    path('strat_reservation/',views.strat_reservation, name='strat_reservation'),
    path('details_booking/<int:id>/',views.get_details_booking,name="details_booking"),
    path('cancel_booking/<int:id>/',views.cancel_booking,name="cancel_booking"),
    path('delete_booking/<int:id>/',views.delete_booking,name="delete_booking")
]