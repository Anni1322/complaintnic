from django.contrib import admin
from .models import User

# Register your models here.
@admin.register(User)
# class UserAdmin(admin.ModelAdmin):
class UserAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'mobile_number', 'gender', 'state', 'district', 'city', 'pin_code')
    search_fields = ('full_name', 'email', 'mobile_number')

