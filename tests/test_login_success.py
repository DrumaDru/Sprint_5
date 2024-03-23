from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import TestLocators

class TestRegistration():

    def test_registration(self, driver, registration_data):
        enter_button = driver.find_element(*TestLocators.ENTER_TO_ACCOUNT_BUTTON)
        enter_button.click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(TestLocators.ENTER_BUTTON_LOGIN))

        registration_link = driver.find_element(*TestLocators.REGISTRATION_LINK)
        registration_link.click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(TestLocators.REGISTRATION_BUTTON))

        input_name = driver.find_element(*TestLocators.INPUT_NAME)
        name = registration_data['name']
        input_name.send_keys(name)

        assert  len(input_name.get_attribute("value")) != 0

        input_email = driver.find_element(*TestLocators.INPUT_EMAIL)
        input_email.click()
        email = registration_data['mail']
        input_email.send_keys(email)

        login_for_male = input_email.get_attribute("value").split("@")[0]
        domen_for_male = input_email.get_attribute("value").split("@")[1]

        assert len(login_for_male) != 0 and domen_for_male == 'ya.ru'

        input_password = driver.find_element(*TestLocators.INPUT_PASSWORD)
        input_password.click()
        password = registration_data['password']
        input_password.send_keys(password)

        assert len(input_password.get_attribute("value")) >= 6

        registration_button = driver.find_element(*TestLocators.REGISTRATION_BUTTON)
        registration_button.click()

        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(TestLocators.ENTER_BUTTON_LOGIN))

        input_email_login = driver.find_element(*TestLocators.INPUT_EMAIL_LOGIN)
        input_email_login.send_keys(email)

        input_password_login = driver.find_element(*TestLocators.INPUT_PASSWORD_LOGIN)
        input_password_login.click()
        input_password_login.send_keys(password)

        enter_button_login  = driver.find_element(*TestLocators.ENTER_BUTTON_LOGIN)
        enter_button_login.click()

        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(TestLocators.CREATE_ORDER))

        create_order = driver.find_element(*TestLocators.CREATE_ORDER)

        assert create_order.text == 'Оформить заказ'