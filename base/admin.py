from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Room)
admin.site.register(Topic)
admin.site.register(Message)


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'username']
