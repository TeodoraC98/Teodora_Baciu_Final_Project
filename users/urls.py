from . import views
from django.contrib.auth import views as auth_views
from django.urls import path
urlpatterns=[
    path('register/',views.register,name='register'),
    path('login/',
          views.log_in, name='login'),
    path('logout/', auth_views.LogoutView.as_view(
        template_name='users/logout.html'),
         name='logout'),
]