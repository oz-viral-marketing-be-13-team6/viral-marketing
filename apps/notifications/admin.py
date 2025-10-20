from django.contrib import admin
from .models import Notification

@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    list_display = ('user', 'name', 'type', 'channel', 'is_read', 'created_at')
    list_filter = ('type', 'channel', 'is_read')
    search_fields = ('name', 'message')
