from django.shortcuts import render,redirect
from django.forms import formset_factory
from bookings.views import  context_reservation_detail
from .forms import PassangerForm
# Create your views here.
list_object_passangers=[]

def info_passengers(request):
   PassangerFormSet=formset_factory(PassangerForm,extra = context_reservation_detail.get("booking").nr_person)
   if request.method=='POST':
      form_passenger_set=PassangerFormSet(request.POST)
      if form_passenger_set.is_valid():
       for form in form_passenger_set:
         passenger=form.save(commit=False)
         list_object_passangers.append(passenger)
       context_reservation_detail["object_passengers"]=list_object_passangers
       return redirect('payment')
      else:
       print("invalid")
      #  ("return http bad request")
       return redirect('info_passengers')
   else:
      form_passenger_set=PassangerFormSet()
      return render(request,'passengers/info_passengers.html',
                    {"context":context_reservation_detail,"form_passenger_set":form_passenger_set})