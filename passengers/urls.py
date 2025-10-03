from django.urls import path
from . import views 
urlpatterns = [
    path('info_passengers/',views.info_passengers, name='info_passengers')
]