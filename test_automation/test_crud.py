import allure  # pip install allure
import pytest  # pip instal pytest
import requests
import allure


@allure.title("TC#1 - Create Booking CRUD Positive ")
@allure.description("TC#1 - Verify the create Booking!")
# @pytest.mark.crud
def test_create_booking_positive_tc1():
    # To make Request
    # URL
    # Method - POST
    # Headers - Content-type=Application/json
    # Payload / Data / Body - Dict / JSON
    # Auth(No)
    base_url = "https://restful-booker.herokuapp.com"
    base_path = "/booking"
    URL = base_url + base_path
    headers = {"Content-Type": "application/json"}
    payload = {
        "firstname": "Jim",
        "lastname": "Brown",
        "totalprice": 111,
        "depositpaid": False,
        "bookingdates": {
            "checkin": "2018-01-01",
            "checkout": "2019-01-01"
        },
        "additionalneeds": "Breakfast"
    }

    response = requests.post(url=URL, headers=headers, json=payload)
    assert response.status_code == 200

    responseData = response.json()
    # Response Body  Verification,
    # Headers
    # Status Code

    bookingid = responseData["bookingid"]
    assert responseData["bookingid"] is not None
    assert responseData["bookingid"] > 0
    assert type(responseData["bookingid"]) == int
    firstname = responseData["booking"]["firstname"]
    lastname = responseData["booking"]["lastname"]
    totalprice = responseData["booking"]["totalprice"]
    depositpaid = responseData["booking"]["depositpaid"]
    assert firstname == "Jim"
    assert lastname == "Brown"
    assert totalprice == 111
    assert depositpaid == False


    checkin = responseData["booking"]["bookingdates"]["checkin"]
    checkout = responseData["booking"]["bookingdates"]["checkout"]
    assert checkin == "2018-01-01"
    assert checkout == "2019-01-01"

@allure.title("TC#2 - Create Booking CRUD Negative payload ")
@allure.description("TC#2 - Verify the create Booking!")
# @pytest.mark.crud
def test_create_booking_positive_tc2():
    base_url = "https://restful-booker.herokuapp.com"
    base_path = "/booking"
    URL = base_url + base_path
    headers = {"Content-Type": "application/json"}
    payload = {}
    response = requests.post(url=URL, headers=headers, json=payload)
    assert response.status_code == 500


@allure.title("TC#3 - Create Booking CRUD Negative payload ")
@allure.description("TC#3 - Verify the create Booking!")

def test_create_booking_stringdata_tc3():
    base_url = "https://restful-booker.herokuapp.com"
    base_path = "/booking"
    URL = base_url + base_path
    headers = {"Content-Type": "application/json"}
    payload = {
        "firstname": "Jim",
        "lastname": "Brown",
        "totalprice": "price",
        "depositpaid": False,
        "bookingdates": {
            "checkin": "2018-01-01",
            "checkout": "2019-01-01"
        },
        "additionalneeds": "Breakfast"
    }

    response = requests.post(url=URL, headers=headers, json=payload)
    assert response.status_code == 200

