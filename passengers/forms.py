from .models import Passenger
from django.forms import ModelForm
from django import forms
class DateInput(forms.DateInput):
    input_type = 'date'


class  PassangerForm(forms.ModelForm):
    class Meta:
        model = Passenger
        fields = ['first_name','last_name','nationality','date_of_birth']
        widgets = {
            'first_name':forms.TextInput(attrs={'class':'form-control'}),
            'last_name':forms.TextInput(attrs={'class':'form-control'}),
            'nationality':forms.TextInput(attrs={'class':'form-control'}),
            'date_of_birth': forms.DateInput(attrs={'class':'form-control', 'type':'date'}),
        }
        # labels={
        #     'nationality': "Nationality",
        #     'first_name':'Name',
        #     'last_name':'Surname',
        # }