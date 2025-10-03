from django.test import TestCase
from .models import CustomUser
from .forms import UserRegisterForm

class UserFormsTests(TestCase):
 def setUpData(self):
    user = CustomUser.objects.create_user(username='user',email='user@yahoo.com', password='password')
    
 def test_user_register(self):
      form_data = {
        'username': 'user', 
        'email': 'user@example.com', 
        'password1': 'errorpassword', 
        'password2': 'errorpassword',
        'first_name':'first_name',
        'last_name':'last_name',
        'contact_number':'877654345',
        'date_of_birth':'2025-09-09' }
      form=UserRegisterForm(data=form_data)
      print(form.errors)
      self.assertTrue(form.is_valid())