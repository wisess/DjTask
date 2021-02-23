from django.contrib import admin
from .models import Message


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = (
        'header',
        'msg_body',
        'is_read',
        'is_send',
        'created',
        'modified',
    )
    ordering = ('created',)
