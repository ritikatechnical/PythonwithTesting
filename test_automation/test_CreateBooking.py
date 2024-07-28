# import pytest
# import allure
# import requests
#
#
# @allure.title("TC #1 For create booking")
# @allure.description("Create booking with valid data")
# @pytest.mark.crud
# def test_create_booking_positive_tc1():
#     base_url = "https://restful-booker.herokuapp.com/"
#     base_path = "booking"
#     url = base_url + base_path
#     headers = {"Contect-Type" : "application/json"}
#     payload = {
#         "firstname" : "Jim",
#         "lastname" : "Brown",
#         "totalprice" : 111,
#         "depositpaid" : True,
#         "bookingdates" : {
#             "checkin" : "2018-01-01",
#             "checkout" : "2019-01-01"
#         },
#         "additionalneeds" : "Breakfast"
#     }
#
#     request = requests.post(url=url, headers=headers, json=payload)
#     assert request.status_code == 200
#     response = request.json()
#     print(response)
#
#
#     assert response["bookingid"]
#     assert response["booking"]["firstname"] == "Jim"
#     assert response["booking"]["lastname"] == "Brown"
#
#
# API Request - HTTP Request

import allure  # pip install allure
import pytest  # pip instal pytest
import requests  # pip install requests


@allure.title("TC#1 - Create Booking with CRUD operation with Positive ")
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
    checkin = responseData["booking"]["bookingdates"]["checkin"]
    checkout = responseData["booking"]["bookingdates"]["checkout"]
    assert firstname == "Jim"
    assert lastname == "Brown"
    assert totalprice == 111
    assert depositpaid == False
    assert checkin == "2018-01-01"
    assert checkout == "2019-01-01"


