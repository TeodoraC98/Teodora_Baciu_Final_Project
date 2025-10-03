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
    reservation=models.ForeignKey(Reservation,on_delete = models.CASCADE,default=1)
    def __str__(self):
        return {f'{self.type}+{self.status}'}
    
    def set_payment_paid(self):
        self.status=self.STATUS.PAID
    def set_payment_cancel(self):
        self.status=self.STATUS.CANCEL