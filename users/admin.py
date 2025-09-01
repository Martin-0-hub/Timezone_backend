from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

# Register your models here.

# admin.register(user)
class CustomUserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        ("Role",{"fields":("role",)}),
    )
    list_display = ("username","email","role","is_active","is_staff","is_superuser")
    list_filter = ("role","is_staff","is_superuser","is_activer")
