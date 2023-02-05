from django.contrib import admin
from .models import CustomUser


# Register your models here.
class CustomerUserAdmin(admin.ModelAdmin):
    model= CustomUser
    list_display = ("username","email","password")

admin.site.register(CustomUser, CustomerUserAdmin)