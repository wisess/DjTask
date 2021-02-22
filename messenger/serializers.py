from rest_framework.serializers import ModelSerializer
from rest_framework.serializers import DateTimeField
from .models import Message


class MessageCreateSerializer(ModelSerializer):
    """Deserialize message data"""

    class Meta:
        model = Message
        fields = ['header', 'msg_body']


class MessageSerializer(ModelSerializer):
    """Deserialize message data"""
    created = DateTimeField(format="%d-%m-%Y %H:%M:%S")
    modified = DateTimeField(format="%d-%m-%Y %H:%M:%S")

    class Meta:
        model = Message
        fields = ['id', 'header', 'msg_body', 'is_send', 'is_read', 'created', 'modified']
