from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ("username", "email", "role", "is_active")
    search_fields = ("username", "email")
    list_filter = ("role", "is_active")
    ordering = ("username",)
