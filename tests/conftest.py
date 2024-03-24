import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from locators import TestLocators
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
import test_data
import random

@pytest.fixture(scope="function")
def driver():
    options = Options()
    options.add_argument('--window-size=1920,1080')
    driver = webdriver.Chrome(options=options)
    #Открываем веб-страницу
    driver.get("https://stellarburgers.nomoreparties.site/")
    yield driver
    #выходим из браузера
    driver.quit()


@pytest.fixture(scope="function")
def registration_data():
    random_number = random.randint(100, 999)
    name = 'Ivan'
    mail = f'{random_number}@ya.ru'
    password = 123456
    failed_password = 12345
    return {'name': name, 'mail': mail, 'password': password, 'failed_password': failed_password}

@pytest.fixture(scope="function")
def registration_page(driver):
    enter_button = driver.find_element(*TestLocators.ENTER_TO_ACCOUNT_BUTTON)
    enter_button.click()
    WebDriverWait(driver, 3).until(
        expected_conditions.visibility_of_element_located(TestLocators.ENTER_BUTTON_LOGIN))
    registration_link = driver.find_element(*TestLocators.REGISTRATION_LINK)
    registration_link.click()
    WebDriverWait(driver, 3).until(
        expected_conditions.visibility_of_element_located(TestLocators.REGISTRATION_BUTTON))

@pytest.fixture(scope="function")
def login_page(driver):
    enter_button = driver.find_element(*TestLocators.ENTER_TO_ACCOUNT_BUTTON)
    enter_button.click()
    WebDriverWait(driver, 3).until(
        expected_conditions.visibility_of_element_located(TestLocators.ENTER_BUTTON_LOGIN))

@pytest.fixture(scope="function")
def personal_account_page(driver, log_in):
    personal_account = driver.find_element(*TestLocators.PERSONAL_ACCOUNT)
    personal_account.click()
    WebDriverWait(driver, 3).until(
        expected_conditions.visibility_of_element_located(TestLocators.PROFILE_TAB))


@pytest.fixture(scope="function")
def log_in(driver, registration_data):
    enter_to_account_button = driver.find_element(*TestLocators.ENTER_TO_ACCOUNT_BUTTON)
    enter_to_account_button.click()
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