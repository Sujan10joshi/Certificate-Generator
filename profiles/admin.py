from django.contrib import admin
from .models import User

# Register your models here.


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'middle_name',
                    'last_name', 'address', 'contact_number', 'email', 'password')
