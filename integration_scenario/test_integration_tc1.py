import allure
import requests
import pytest


# ---------------Verify with create booking the patch booking and Verify with first name-------------

@allure.title("Resful Booker Project Create Booking TC #1")
def test_create_booking():
    base_url = "https://restful-booker.herokuapp.com/"
    path_url = "booking/"
    url = base_url + path_url
    headers = {'Content-Type': 'application/json'}
    json_payload = {
        "firstname": "Princy",
        "lastname": "Gupta",
        "totalprice": 111,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2018-01-01",
            "checkout": "2019-01-01"
        },
        "additionalneeds": "Breakfast"
    }
    responseDate = requests.post(url=url, headers=headers, json=json_payload)
    assert responseDate.status_code == 200
    data = responseDate.json()
    print(data)
    assert data['booking']['firstname'] == 'Princy'
    print("first name is confirmed")

