from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import time

driver = webdriver.Chrome()
driver.get("https://stellarburgers.nomoreparties.site/")

#найти на странице кнопку для входа и клинуть по ней
driver.find_element(By.XPATH, ".//button[text()='Войти в аккаунт']").click()


# Добавь явное ожидание для проверки перехода на форму заполнения логина и пароля
WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, ".//h2[text()='Вход']")))

#ввод в поле  email значения
driver.find_element(By.XPATH, "//label[text()='Email']/following-sibling::input").click()

email_input = driver.find_element(By.XPATH, "//label[text()='Email']/following-sibling::input")

email_input.send_keys("andrey_maksimo_6_777@yandex.ru")


#ввод в поле Пароль значения
driver.find_element(By.XPATH, "//label[text()='Пароль']/following-sibling::input").click()

password_input = driver.find_element(By.XPATH, "//label[text()='Пароль']/following-sibling::input")

password_input.send_keys('MaVburgers7Op280291')

#Поиск кнопки Войти и клик по ней

driver.find_element(By.XPATH, ".//button[text()='Войти']").click()

WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, ".//button[text()='Оформить заказ']")))

#Поиск кнопки Личный кабинет и клик по ней
driver.find_element(By.XPATH, ".//p[text() = 'Личный Кабинет']").click()

# Добавь явное ожидание для проверки перехода в личный кабинет
WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, ".//a[text()='Профиль']")))

#Найти Лого и кликнуть по нему
driver.find_element(By.CLASS_NAME, 'AppHeader_header__logo__2D0X2').click()

WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, ".//button[text()='Оформить заказ']")))

assert driver.find_element(By.XPATH, ".//button[text()='Оформить заказ']").text == 'Оформить заказ'


time.sleep(5)

driver.quit()