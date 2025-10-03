from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm
from .models import CustomUser
from django import forms
class DateInput(forms.DateInput):
    input_type = 'date'


class   UserRegisterForm(UserCreationForm):
    password1 = forms.CharField(
        label=' Password',
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password',
                                          'class':'form-control',
                                          'id':'id_password1',
                                            'required':True}),
    )
    password2 = forms.CharField(
        label=' Confirm password',
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password',
                                          'class':'form-control',
                                          'id':'id_password2',
                                           'required':True}),
    )
    class Meta:
        model = CustomUser
        fields = ['username','email','first_name','last_name','date_of_birth','contact_number']
        
        widgets = {
            'username' : forms.TextInput(attrs={'class':'form-control', 'required':True}),
            'email' : forms.EmailInput(attrs={'class':'form-control', 'required':True}),
            'first_name':forms.TextInput(attrs={'class':'form-control', 'required':True}),
            'last_name':forms.TextInput(attrs={'class':'form-control', 'required':True}),
            'contact_number':forms.TextInput(attrs={'class':'form-control', 'required':True}),
            'date_of_birth': DateInput(attrs={'class':'form-control', 'required':True}),

        }
        labels={
            'email': "Email",
            'first_name':'Name',
            'last_name':'Surname',
            'contact_number':'Phone',
            'date_of_birth':'Birth date'
        }

class   UserChangeForm(UserChangeForm):
    password1 = forms.CharField(
        label=' Password',
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password','class':'form-control','id':'id_password1'}),
    )
    password2 = forms.CharField(
        label=' Confirm password',
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password','class':'form-control','id':'id_password2'}),
    )
    class Meta:
        model = CustomUser
        fields = ['username','email','first_name','last_name','date_of_birth','contact_number']
        
        widgets = {
            'username' : forms.TextInput(attrs={'class':'form-control'}),
            'email' : forms.EmailInput(attrs={'class':'form-control'}),
            'first_name':forms.TextInput(attrs={'class':'form-control'}),
            'last_name':forms.TextInput(attrs={'class':'form-control'}),
            'contact_number':forms.TextInput(attrs={'class':'form-control'}),
            'birth_date':forms.DateField(),

        }
        labels={
            'email': "Email",
            'first_name':'Name',
            'last_name':'Surname',
            'contact_number':'Phone number',
            'birth_date':'Date of birth'
        }

class   UserUpdateForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['username','email','first_name','last_name','date_of_birth','contact_number']
        
        

class   UserCustomLoginForm(forms.Form):
    email = forms.EmailField(widget=forms.TextInput(attrs={'class': 'form-control frm-input',
                                                           'placeholder': 'Email', 
                                                           'required':True}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control frm-input',
                                                                 'placeholder':'Password', 
                                                                 'required':True}))
