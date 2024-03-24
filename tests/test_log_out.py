import pytest
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import TestLocators

class TestLogOut:
    def test_log_out(self, driver, log_in, personal_account_page):
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(TestLocators.LOG_OUT_BUTTON))

        log_out_button = driver.find_element(*TestLocators.LOG_OUT_BUTTON)
        log_out_button.click()

        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(TestLocators.ENTER_BUTTON_LOGIN))

        enter_button_login = driver.find_element(*TestLocators.ENTER_BUTTON_LOGIN)

        assert enter_button_login.text == 'Войти'

