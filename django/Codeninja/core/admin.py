from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUsuario, Service


# Register your models here.
admin.site.register(Service)


class CustomUsuarioAdmin(UserAdmin):
    list_display = ('username', 'name', 'email', 'is_staff', 'is_active')
    search_fields = ('username', 'name', 'email')


admin.site.register(CustomUsuario, CustomUsuarioAdmin)
