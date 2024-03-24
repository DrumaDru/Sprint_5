import pytest
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import TestLocators

class TestRegistrationPasswordFailed:
    def test_password_failed(self, driver, registration_page, registration_data):
        input_name = driver.find_element(*TestLocators.INPUT_NAME)
        name = registration_data['name']
        input_name.send_keys(name)

        input_email = driver.find_element(*TestLocators.INPUT_EMAIL)
        input_email.click()
        email = registration_data['mail']
        input_email.send_keys(email)

        input_password = driver.find_element(*TestLocators.INPUT_PASSWORD)
        input_password.click()
        failed_password = registration_data['failed_password']
        input_password.send_keys(failed_password)

        registration_button = driver.find_element(*TestLocators.REGISTRATION_BUTTON)
        registration_button.click()

        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((TestLocators.FAILED_PASSWORD_TEXT)))

        failed_password_text = driver.find_element(*TestLocators.FAILED_PASSWORD_TEXT)

        assert failed_password_text.text == 'Некорректный пароль'


