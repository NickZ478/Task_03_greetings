from django.contrib import admin
from .models import UserName

@admin.register(UserName)
class UserNameAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at')
    search_fields = ('name',)
    list_filter = ('created_at',)