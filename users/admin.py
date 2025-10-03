from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser,Costumer,Manager,Employee
from .forms import  UserRegisterForm,UserChangeForm
# Register your models here.
class CustomUserAdmin(UserAdmin):
    add_form =  UserRegisterForm
    form =  UserChangeForm
    model = CustomUser
    list_display = ("email","last_name","first_name","type","date_of_birth","contact_number", "is_staff", "is_active",)
    list_filter = ("email", "is_staff", "is_active","is_admin")
    fieldsets = (
        (None, {"fields": ("email", "password")}),
        ("Permissions", {"fields": ("is_staff", "is_active","is_admin", "groups", "user_permissions")}),
    )
    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": (
                "email","last_name","first_name","type","date_of_birth","contact_number","password1", "password2", "is_staff",
                "is_active",
            )}
        ),
    )
    search_fields = ("email",)
    ordering = ("email",)
admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Costumer)
admin.site.register(Manager)
admin.site.register(Employee)