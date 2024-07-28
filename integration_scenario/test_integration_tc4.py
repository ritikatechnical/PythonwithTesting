  # --------------Invalid Creation - enter a wrong payload or Wrong JSON.---------------

import allure
import requests


@allure.title("Create Booking with wrong payload")
def test_create_booking_withwrong_payload():
    url = "https://restful-booker.herokuapp.com/booking"
    headers = {"Content-Type": "application/json"}
    payload = {
        "firstname": 7877,
        "lastname": "Nashi",
        "totalprice": 111,
        "depositpaid": True,
        "bookingdates": {
            "checkin": 0,
            "checkout": ""
        },
        "additionalneeds": "Breakfast"
    }

    response = requests.post(url=url, headers=headers, json=payload)
    assert response.status_code == 500

