from datetime import datetime, timezone
from django.db import models
from .models import Message


def create_message(msg_data):
    """Create message in DB"""
    today = datetime.now()
    msg_instance, created = Message.objects.get_or_create(header=msg_data.get("header"),
                                                          msg_body=msg_data.get("msg_body"))
    msg_instance.header = msg_data.get("header")
    msg_instance.msg_body = msg_data.get("msg_body")
    msg_instance.is_send = False
    msg_instance.is_read = False
    msg_instance.created = today
    msg_instance.modified = today
    msg_instance.save()

    return msg_instance.id


def get_msg_by_id(msg_id):
    """Get message by id from DB"""
    try:
        return Message.objects.get(id=msg_id)
    except models.ObjectDoesNotExist:
        return False


def msg_is_send_mark(msg_id):
    """Mark is_send flag for message by id"""
    msg = get_msg_by_id(msg_id)
    if msg:
        msg.is_send = True
        msg.save()
        return msg.id
    return 0


def msg_is_read_mark(msg_id):
    """Mark is_read flag for message by id"""
    msg = get_msg_by_id(msg_id)
    if msg:
        msg.is_read = True
        msg.save()
        return msg
    return None


def get_msg_list():
    """Get all messages"""
    try:
        return Message.objects.order_by('created').all()
    except models.ObjectDoesNotExist:
        return False


def delete_msg_by_id(msg_id):
    """Delete message by id"""
    try:
        msg = get_msg_by_id(msg_id)
        if msg:
            msg.delete()
            return True
    except models.ObjectDoesNotExist:
        return False


def change_msg_data(msg_id, msg_data):
    """Change message data by id"""
    msg = get_msg_by_id(msg_id)
    if msg:
        msg.header = msg_data.get("header")
        msg.msg_body = msg_data.get("msg_body")
        msg.modified = datetime.now(timezone.utc)
        msg.save()
        return msg
    return None
