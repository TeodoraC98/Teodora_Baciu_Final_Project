from django.db import models
from django.utils import timezone
from bookings.models import Reservation
# Create your models here.

class Payment(models.Model):
    PENDING='PENDING'
    PAID='PAID'
    CANCEL='CANCEL'
    STATUS={
        PENDING:'Pending',
        PAID:'Paid',
        CANCEL:'Cancel',
    }
    amount=models.FloatField(null=False, default=0.0)
    date=models.DateField(null=False, auto_now_add=True)
    status=models.CharField(max_length=50,null=False,default='Pending',choices=STATUS)
    type=models.CharField(max_length=50,null=False)
    reservation=models.ForeignKey(Reservation,on_delete = models.CASCADE,blank=True)

    def __str__(self):
        return f'{self.type}'
    
    def set_booking(self,booking):
        self.reservation=booking
        self.save()

    def get_payment_by_booking(nr_reservation):
       try:
          payment=Payment.objects.filter(reservation=nr_reservation)
          return payment
       except:
          print("Error selecting the payment")

    # def set_payment_paid(self):
    #     try:
    #      self.status=self.STATUS.PAID
    #      self.save()
    #     except:
    #        print("ERROR SETING THE PAYMENT WITH STATUS PAID")

    # def set_payment_cancel(self):
    #    try:
    #     self.status=self.STATUS.CANCEL
    #     self.save()
    #    except:
    #        print("ERROR SETING THE PAYMENT WITH STATUS CANCEL")

    def cancel_payment(reservation):
       try:
          payment=Payment.objects.get(reservation=reservation)
          payment.status = 'CANCEL'
          payment.save()
       except:
          print("ERORR CHANGHING STATUS BOOKING")
    def set_payment_paid(reservation):
       try:
          payment=Payment.objects.get(reservation=reservation)
          print(payment)
          payment.status = 'PAID'
          payment.save()
       except:
          print("ERROR SETTING THE PAYMENT WITH STATUS PAID")
