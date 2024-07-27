#put
#url
#bookingId
#hearder
#token
#payload

import allure
import requests

@allure.title("TC #1 Restful Booker update Booking")
@allure.description("TC#1 - Verify the updated Booking by booking id!")
def create_token():
    url = "https://restful-booker.herokuapp.com/auth"
    header = {'Content-Type' : 'application/json'}
    payload = {
        "username" : "admin",
        "password" : "password123"
    }
    response = requests.post(url=url, headers=header, json=payload)
    token = response.json()["token"]
    print(token)
    return token

def create_bookingid():
    print("Create Booking Testcase")
    base_url = "https://restful-booker.herokuapp.com/"
    path = "booking"
    url = base_url + path
    header   = {'Content-Type' : 'application/json'}
    payload = {
        "firstname": "Amit",
        "lastname": "Brown",
        "totalprice": 111,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2018-01-01",
            "checkout": "2019-01-01"
        },
        "additionalneeds": "Breakfast"
    }
    response = requests.post(url=url , headers=header, json=payload)
    assert response.status_code == 200
    print(type(url))
    print(type(payload))
    print(type(header))
    print(type(response))
    data = response.json()
    return data["bookingid"]

def test_put_create_booking():
    print("Updating  created booking")
    base_url ="https://restful-booker.herokuapp.com"
    path = "/booking/" + str(create_bookingid())
    url = base_url + path
    header = {"Content-Type" : "application/json", "Cookie" : "token=" + create_token()}
    payload = {
        "firstname": "Charly",
        "lastname": "Brown",
        "totalprice": 111,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2018-01-01",
            "checkout": "2019-01-01"
        },
        "additionalneeds": "Breakfast"
    }
    response = requests.put(url=url, headers=header, json=payload)
    assert response.status_code == 200
    data = response.json()
    print(data)
    assert data["firstname"] == "Charly"


def test_delete_created_booking():
    print("Deleting created booking")
    base_url = "https://restful-booker.herokuapp.com"
    path = "/booking/" + str(create_bookingid())
    Delete_url = base_url + path
    header = {"Content-Type": "application/json", "Cookie": "token=" + create_token()}
    print(header)
    response = requests.delete(url=Delete_url, headers=header)
    assert response.status_code == 201  # 201 Created

