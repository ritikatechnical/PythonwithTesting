# we need to verify test case

import pytest
import allure


@allure.title("Test Case#1 Addition")
@allure.description("Verify Addition functionality")
@pytest.mark.smoke
def test_addition():
    # assert - keyword is verify which is present in pytest and verify Actual result == Expected result.clesr
    assert 2 + 3 == 5, "Addition failed"


@allure.title("Test Case#2 substraction")
@allure.description("Verify substraction functionality")
@pytest.mark.smoke
def test_subtraction1():
    assert 6 - 3 == 3, "Subtraction failed"


@allure.title("Test Case#3 Addition")
@allure.description("Verify subtraction 5-3=2 functionality")
@pytest.mark.regression
def test_subtraction2():
    assert 5 - 3 == 2, "Subtraction failed"


@allure.title("Test Case#3 Addition")
@allure.description("Verify sub functionality")
@pytest.mark.snity
def test_subtraction3():
    assert 6 - 3 == 3, "Subtraction failed"


@allure.title("Test Case#4 Addition")
@allure.description("Verify subtraction 5-3=2 functionality")
@pytest.mark.skip(reason="I don't want to execute this test case")
def test_subtraction4():
    assert 5 - 3 == 2, "Subtraction failed"
