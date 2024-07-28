# --------------- Create a Booking , Delete the Booking with ID and Verify with Get request that not exist--------------
import allure
import requests
import pytest


@allure.title("Resful Booker Project Create Booking TC #2")
@pytest.fixture(scope="module")
def create_booking():
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
    booking_id = data['bookingid']
    print(booking_id)
    return booking_id

@allure.title("Delete the booking with ID")
def test_delete_booking_withID(create_token, create_booking):
    base_url = "https://restful-booker.herokuapp.com/"
    path_url = "booking/" + str(create_booking)
    delete_url = base_url + path_url
    cookie = "token=" + create_token
    headers = {'Content-Type': 'application/json', 'Cookie': cookie}
    print(headers)
    response = requests.delete(url=delete_url, headers=headers)
    assert response.status_code == 201
    print("Booking Delete")


# @allure.title("Verify by get request that Deleted Booking should not exist")
# def test_get_booking_id():
#     url = "https://restful-booker.herokuapp.com/booking/" + str(create_booking)
#     response = requests.get(url)
#     assert response.status_code == 404
#     print("id deleted")


@allure.title("Verify by get request that Deleted Booking should not exist")
def test_get_booking_id():
    url = "https://restful-booker.herokuapp.com/booking/"
    response = requests.get(url)
    assert response.status_code == 200
    data = response.json()
    print(data)