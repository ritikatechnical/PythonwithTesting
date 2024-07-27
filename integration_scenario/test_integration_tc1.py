import allure
import requests
import pytest

def create_token():

    url = "https://restful-booker.herokuapp.com/auth"
    data = {
        "username": "admin",
        "password": "password123"
    }
    response = requests.post(url=url, json=data)
    token = response.json()["token"]
    return token

