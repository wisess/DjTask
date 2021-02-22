from celery import shared_task
from .services import msg_is_send_mark


@shared_task
def send_msg_to_ext_system(msg_id):
	"""Async sending message to external system"""
	msg_is_send_mark(msg_id) 
