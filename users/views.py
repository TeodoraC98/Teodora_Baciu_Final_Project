from django.shortcuts import render, redirect
from .forms import UserRegisterForm, UserCustomLoginForm
from django.contrib.auth import authenticate, login
from django.contrib import messages
def register(request):
    if request.method=='POST':
        user_register_form=UserRegisterForm(request.POST)
        if user_register_form.is_valid():
            user=user_register_form.save()
            # set group
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
    