import pytest
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import TestLocators
import test_data



class TestEnterToAccount():
    #проверка входа в аккаунт через кнопку "Войти в акккаунт" на главной стрнице.
    def test_login_by_button_enter(self, driver, log_in):
        create_order = driver.find_element(*TestLocators.CREATE_ORDER)

        assert create_order.text == 'Оформить заказ'

    #проверка входа в аккаунт через кнопку "Личный аккаунт".
    def test_personal_account_enter(self, driver):
        personal_account = driver.find_element(*TestLocators.PERSONAL_ACCOUNT)
        personal_account.click()

        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(TestLocators.ENTER_BUTTON_LOGIN))

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

    #проверка входа в аккаунт через гиперссылку "войти", на странице регистрации
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

    #проверка входа в аккаунт через гипперсылку "войти", на странице восстановления пароля
    def test_new_password_enter_button(self, driver, login_page):
        new_password_link = driver.find_element(*TestLocators.NEW_PASSWORD_LINK)
        new_password_link.click()

        new_password_enter_button = driver.find_element(*TestLocators.NEW_PASSWORD_ENTER_BUTTON)
        new_password_enter_button.click()

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