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

#нешел гиперссылку для регистрации и кликнул по ней
driver.find_element(By.CLASS_NAME, "Auth_link__1fOlj").click()

# Добавь явное ожидание для проверки перехода на форму регистрации
WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, ".//h2[text()='Регистрация']")))

#ввод в поле Пароль невалидное значение
driver.find_element(By.XPATH, "//label[text()='Пароль']/following-sibling::input").click()

password_input = driver.find_element(By.XPATH, "//label[text()='Пароль']/following-sibling::input")

password_input.send_keys('12345')

#Поиск кнопки Зарегистрировать и клик по ней
driver.find_element(By.XPATH, ".//form//button[text()='Зарегистрироваться']").click()

WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, ".//form//p[text()='Некорректный пароль']")))

false_element = driver.find_element(By.XPATH, ".//form//p[text()='Некорректный пароль']")

assert false_element.text == 'Некорректный пароль'

time.sleep(5)

driver.quit()
