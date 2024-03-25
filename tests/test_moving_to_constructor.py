import pytest
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import TestLocators

class TestMovingToConstructor:
    #проверка перехода в конструктор из личного кабинета
    def test_constructor_button(self, driver, personal_account_page):
        constructor_button = driver.find_element(*TestLocators.CONSTRUCTOR_BUTTON)
        constructor_button.click()

        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(TestLocators.CREATE_ORDER))

        create_order = driver.find_element(*TestLocators.CREATE_ORDER)

        assert create_order.text == 'Оформить заказ'

    #проверка перехода из личного кабинета в конструктор через логотип
    def test_logo(self, driver, personal_account_page):
        logo = driver.find_element(*TestLocators.LOGO)
        logo.click()

        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(TestLocators.CREATE_ORDER))

        create_order = driver.find_element(*TestLocators.CREATE_ORDER)

        assert create_order.text == 'Оформить заказ'