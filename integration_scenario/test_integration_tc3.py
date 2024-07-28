#    ----------------Create a BOOKING, Delete It-----------


import pytest
import allure
import requests


@allure.title("Resful Booker Project Create Booking TC #1")
def test_create_booking():
    base_url = "https://restful-booker.herokuapp.com/"
    path_url = "booking/"
    url = base_url + path_url
    headers = {'Content-Type': 'application/json'}
    json_payload = {
        "firstname": "Mohan",
        "lastname": "aggarwal",
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


def test_delete_created_booking(create_token):
    print("Deleting created booking")
    base_url = "https://restful-booker.herokuapp.com"
    path = "/booking/" + str(test_create_booking())
    Delete_url = base_url + path
    header = {"Content-Type": "application/json", "Cookie": "token=" + create_token}
    print(header)
    response = requests.delete(url=Delete_url, headers=header)
    assert response.status_code == 201
    print("id deleted")

def test_Get_deleted_id():
    base_url = "https://restful-booker.herokuapp.com/booking/"
    response = requests.get(base_url)
    data = response.json()
    print(data)
    assert response.status_code == 200
