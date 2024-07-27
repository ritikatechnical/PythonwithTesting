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
    print(responseData.headers)
    print(responseData.status_code)
    print(responseData.cookies)
    print(responseData.json())
    assert responseData.status_code == 200