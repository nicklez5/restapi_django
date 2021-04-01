from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import CustomUser, Job, Machine,Timecard

class AdminAccount(UserAdmin):
    list_display = ('username', 'name','is_admin')
    search_fields = ('username')
    readonly_fields = ()
    filter_horizontal = ()

# Register your models here.
