from functools import reduce

import requests

SOME_ITERATOR = 99


def get_url():
    ...


def get_data_from_url(param) -> list:
    try:
        response = requests.get(param).json()
        return response
    except Exception:
        raise Exception("Create your custom exception here")


def get_all_data(param):
    """classic way"""
    all_data = []
    for i in range(SOME_ITERATOR):
        all_data += get_data_from_url(param)
    return all_data


def get_all_data_(param):
    """functional way"""
    reduce(lambda x, y: x + y, list(map(get_data_from_url, param)), [])
