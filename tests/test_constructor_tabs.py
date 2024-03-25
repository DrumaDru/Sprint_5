import pytest
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import TestLocators

class TestTabs:
    def test_souse_tab(self, driver, log_in):
        souse_tab = driver.find_element(*TestLocators.SOUSE_TAB)
        souse_tab.click()

        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(TestLocators.CURRENT_TAB))

        current_tab = driver.find_element(*TestLocators.CURRENT_TAB).get_attribute('class')

        assert 'current' in current_tab

    def test_bread_tab(self, driver, log_in):
        souse_tab = driver.find_element(*TestLocators.SOUSE_TAB)
        souse_tab.click()

        bread_tab = driver.find_element(*TestLocators.BREAD_TAB)
        bread_tab.click()

        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(TestLocators.CURRENT_TAB))

        current_tab = driver.find_element(*TestLocators.CURRENT_TAB).get_attribute('class')

        assert 'current' in current_tab

    def test_filling_tab(self, driver, log_in):
        filling_tab = driver.find_element(*TestLocators.FILLING_TAB)
        filling_tab.click()

        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(TestLocators.CURRENT_TAB))

        current_tab = driver.find_element(*TestLocators.CURRENT_TAB).get_attribute('class')

        assert 'current' in current_tab




