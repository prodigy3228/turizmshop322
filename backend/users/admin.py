from django.contrib import admin
from .models import Profile

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'phone_number']
    search_fields = ['user__username', 'user__email', 'phone_number']

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

# Разрегистрируем стандартную модель, если она уже зарегистрирована
if admin.site.is_registered(User):
    admin.site.unregister(User)

# Зарегистрируем заново со стандартным UserAdmin
@admin.register(User)
class CustomUserAdmin(UserAdmin):
    pass