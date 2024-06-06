from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from .models import Trip, Place
# Register your models here.

User = get_user_model()

# Unregister the User model first if it's already registered
try:
    admin.site.unregister(User)
except admin.sites.NotRegistered:
    pass

admin.site.register(User, UserAdmin)
admin.site.register(Trip)
admin.site.register(Place)