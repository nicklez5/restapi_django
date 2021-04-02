from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import CustomUser, Job, Machine,Timecard

class AdminAccount(UserAdmin):
    list_display = ('username', 'name','is_admin')
    search_fields = ('username')
    readonly_fields = ('id')
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

admin.site.register(Job)
admin.site.register(Machine)
admin.site.register(Timecard)
admin.site.register(CustomUser)

# Register your models here.
