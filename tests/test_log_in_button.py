from locators import TestLocators


class TestLoginButtonEnter():

    def test_login_by_button_enter(self, driver, log_in):
        create_order = driver.find_element(*TestLocators.CREATE_ORDER)

        assert create_order.text == 'Оформить заказ'