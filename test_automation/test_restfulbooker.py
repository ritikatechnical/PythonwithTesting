import pytest
import allure
import requests


@allure.title("Restfull Booker Project#1, TC Get Request")
@allure.description("TC #1, Verify Get Request with ID works")
@allure.tag("smoke", "regerssion" "p0")
@allure.label("owner", "Ritika")
@allure.testcase("TC #1")
def test_get_requestby_id():
    url = "https://restful-booker.herokuapp.com/booking/1"
    responseData = requests.get(url)
    print(responseData.text)
    print(responseData.json())
    assert responseData.status_code == 200


@allure.title("Restfull Booker Test Cases #2")
@allure.description("TC #2, Verify Get Request with invalid ID")
@allure.tag("regerssion" "p0"  "smoke")
@allure.label("owner", "Ritika")
@allure.testcase("TC #2")
def test_get_requestby_invalid_id():
    url = "https://restful-booker.herokuapp.com/booking/invalud"
    responseData = requests.get(url)
    print(responseData.text)
    assert responseData.status_code == 404
