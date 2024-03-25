import pytest
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import TestLocators

class TestPersonalAccount:
    def test_personal_account(self, driver, personal_account_page):
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(TestLocators.PROFILE_TAB))

        profile_tab = driver.find_element(*TestLocators.PROFILE_TAB)

        assert profile_tab.text == "Профиль"

