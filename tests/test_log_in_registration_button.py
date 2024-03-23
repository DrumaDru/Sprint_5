from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import test_data
from locators import TestLocators

class TestEnterButtonRegistrationPage:
    def test_enter_button_registration_page(self, driver, registration_page):
        enter_button_link = driver.find_element(*TestLocators.ENTER_LINK)
        enter_button_link.click()
        input_email_login = driver.find_element(*TestLocators.INPUT_EMAIL_LOGIN)
        email = test_data.email
        input_email_login.send_keys(email)
        input_password_login = driver.find_element(*TestLocators.INPUT_PASSWORD_LOGIN)
        password = test_data.password
        input_password_login.send_keys(password)
        enter_button_login = driver.find_element(*TestLocators.ENTER_BUTTON_LOGIN)
        enter_button_login.click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(TestLocators.CREATE_ORDER))
        create_order = driver.find_element(*TestLocators.CREATE_ORDER)

        assert create_order.text == 'Оформить заказ'


