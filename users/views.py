from django.shortcuts import render, redirect
from .forms import UserRegisterForm, UserCustomLoginForm
from .models import Costumer
from django.contrib.auth.models import Group
from django.contrib.auth import authenticate, login
from django.contrib import messages
def register(request):
    if request.method=='POST':
        user_register_form=UserRegisterForm(request.POST)
        if user_register_form.is_valid():
            username=request.POST['username']
            email=request.POST['email']
            first_name=request.POST['first_name']
            last_name=request.POST['last_name']
            contact_number=request.POST['contact_number']
            date_of_birth=request.POST['date_of_birth']
            password=request.POST['password1']
            user=Costumer.objects.create_user(username=username,email=email,password=password,
                                              first_name=first_name,last_name=last_name,
                                              contact_number=contact_number,date_of_birth=date_of_birth)
            user.save()
            user.groups.add(Group.objects.get(name='Customer'))
            messages.success(request,f'Thank you for creating an account with us!')
            return redirect('login')
    else:
            user_register_form = UserRegisterForm()
    return render(request,'users/register.html',{'user_form':user_register_form})

def log_in(request):
     if request.method=='POST':
        email = request.POST["email"]
        password = request.POST["password"]
        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request,user)
            return redirect('index')
        else:
            messages.success(request,f'Invalid email or password. Please try again!')
            return redirect('login')
     else:
        form_login=UserCustomLoginForm()
        context={
            "login_form":form_login
        }
        return render(request,'users/login.html',context=context)
    