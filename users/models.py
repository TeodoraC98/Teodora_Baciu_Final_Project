from django.db import models
from django.contrib.auth.models import AbstractUser,Group
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import BaseUserManager
from .managers import UserManagerCustom
from django.utils.translation import gettext_lazy as _

class CustomUser(AbstractUser):
  class Types(models.TextChoices):
        CUSTOMER = "CUSTOMER" , "costumer"
        EMPLOYEE = "EMPLOYEE" , "employee"
        MANAGER="MANAGER","manager"
  username = models.CharField(null=True,blank=True)
  email = models.EmailField(_('email address'), unique = True,max_length=100)
  contact_number = models.CharField(max_length = 10)
  date_of_birth=models.DateField(null=True,blank=True)
  type = models.CharField(max_length = 8 , choices = Types.choices , 
                           default = Types.CUSTOMER)
  is_active = models.BooleanField(default = True)
  is_admin = models.BooleanField(default =False)
  is_staff = models.BooleanField(default =False)
  is_superuser = models.BooleanField(default = False)
  is_customer = models.BooleanField(default = False)
  is_employee = models.BooleanField(default = False)
  is_manager = models.BooleanField(default = False)

  USERNAME_FIELD = 'email'
  REQUIRED_FIELDS = ['username', 'first_name', 'last_name']
  objects = UserManagerCustom()

  def __str__(self):
      return "{}".format(self.email)
  def has_perm(self , perm, obj = None):
        return self.is_admin
  def has_module_perms(self , app_label):
        return True

class CostumerManager(BaseUserManager):
    def create_user(self, email, password, **extra_fields):
        if not email or len(email) <= 0 : 
            raise ValueError(_("Please provide an email!"))
        if not password :
            raise ValueError("Please provide a password!")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user
    
    def get_queryset(self , *args,  **kwargs):
        queryset = super().get_queryset(*args , **kwargs)
        queryset = queryset.filter(type =CustomUser.Types.CUSTOMER)
        return queryset    
    
class EmployeeManager(BaseUserManager):
    def create_user(self, email, password, **extra_fields):
        if not email or len(email) <= 0 : 
            raise  ValueError(_("Please provide an email!"))
        if not password :
            raise ValueError("Please provide a password!")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user
      
    def get_queryset(self , *args , **kwargs):
        queryset = super().get_queryset(*args , **kwargs)
        queryset = queryset.filter(type = CustomUser.Types.EMPLOYEE)
        return queryset
    
class ManagerManager(BaseUserManager):
    def create_user(self, email, password, **extra_fields):
        if not email or len(email) <= 0 : 
            raise  ValueError(_("Please provide an email!"))
        if not password :
            raise ValueError("Please provide a password!")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user
      
    def get_queryset(self , *args , **kwargs):
        queryset = super().get_queryset(*args , **kwargs)
        queryset = queryset.filter(type = CustomUser.Types.MANAGER)
        return queryset  
      
class Costumer(CustomUser):
    class Meta : 
        proxy = True
    objects = CostumerManager()
    
    def save(self , *args , **kwargs):
        self.type = CustomUser.Types.CUSTOMER
        self.is_customer = True
        self.groups.add(Group.objects.get(name='Customer'))
        return super().save(*args , **kwargs)
    
    
class Employee(CustomUser):
    class Meta :
        proxy = True
    objects = EmployeeManager()
    
    def save(self  , *args , **kwargs):
        self.type = CustomUser.Types.EMPLOYEE
        self.is_employee = True
        self.groups.add(Group.objects.get(name='Employee'))
        return super().save(*args , **kwargs)
    
class Manager(CustomUser):
    class Meta :
        proxy = True
    objects = ManagerManager()
    
    def save(self  , *args , **kwargs):
        self.type = CustomUser.Types.MANAGER
        self.is_manager = True
        self.is_admin = True
        self.groups.add(Group.objects.get(name='Manager'))
        return super().save(*args , **kwargs)