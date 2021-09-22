from celery import shared_task
from .services import msg_is_send_mark
import requests


@shared_task
def send_msg_to_ext_system(msg_id):
	"""Async sending message to external system"""
	msg_is_send_mark(msg_id)


@shared_task
def get_symbol_data():
	"""Request symbol data"""
	symbols = ['BTCUSDT', 'ETHUSDT']
	analyze_data = {}
	for symbol in symbols:
		url = f'https://api.binance.com/api/v3/ticker/price?symbol={symbol}'
		response = requests.get(url)
		data = response.json().get("price")
		analyze_data[symbol] = data
	return analyze_data
