from django.contrib import admin
from .models import *


@admin.register(Locomotive)
class Admin(admin.ModelAdmin):
    list_display = ('name', 'ip_address', 'active')

