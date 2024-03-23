from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import TestLocators
import time

class TestLogo:
    def test_logo(self, driver, personal_account_page):
        logo = driver.find_element(*TestLocators.LOGO)
        logo.click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(TestLocators.CREATE_ORDER))
        create_order = driver.find_element(*TestLocators.CREATE_ORDER)
        time.sleep(3)

        assert create_order.text == 'Оформить заказ'