import configuration
import requests


def create_order(order_data):
    return requests.post(configuration.API_URL + configuration.API_CREATE_ORDER, json=order_data)


def get_order(track):
    return requests.get(configuration.API_URL + configuration.API_GET_ORDER, params=dict(t=track))
