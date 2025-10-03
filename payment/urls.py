from django.urls import path
from . import views 
urlpatterns = [
    path('get_payment_information/',views.get_payment_information, name='payment'),
    path('success_payment/',views.success_payment,name='success'),
    path('cancel_payment/',views.cancel_payment,name='cancel')
]