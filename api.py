import requests
import json


def new_results():
    data_lst = list()

    for i in range(10):
        response = requests.get('http://www.boredapi.com/api/activity/')
        data = response.json()
        data_lst.append(data)

    return data_lst


def get_activity(data):
    activity = data["activity"]
    return activity


def get_key(data):
    key = data["key"]
    return key
