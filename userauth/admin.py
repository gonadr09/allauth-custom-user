from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser

# Register your models here.

class CustomUserAdmin(UserAdmin):
    add_form = UserCreationForm
    form = UserChangeForm
    mode = CustomUser
    list_display = ['pk', 'email', 'username', 'first_name', 'last_name']
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('email', 'first_name', 'last_name', 'birthday', 'address', 'zip_code', 'city', 'country', 'price_list')}),
    )
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('birthday', 'address', 'zip_code', 'city', 'country', 'price_list')}),
    )

admin.site.register(CustomUser, CustomUserAdmin)