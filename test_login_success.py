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

#ввод в поле имя значения и проверка, что оно не пустое
name_input = driver.find_element(By.XPATH, "//label[text()='Имя']/following-sibling::input")

name_input.send_keys('Terminator')

assert len(name_input.get_attribute("value")) != 0

#ввод в поле  email значения и проврка на валидность
driver.find_element(By.XPATH, "//label[text()='Email']/following-sibling::input").click()

email_input = driver.find_element(By.XPATH, "//label[text()='Email']/following-sibling::input")

email_input.send_keys("andre_maksimov_6_123@ya.ru")

login = email_input.get_attribute("value").split("@")[0]

assert len(login) != 0 and "ya.ru" in email_input.get_attribute("value")

#ввод в поле Пароль значения и проврка на валидность
driver.find_element(By.XPATH, "//label[text()='Пароль']/following-sibling::input").click()

password_input = driver.find_element(By.XPATH, "//label[text()='Пароль']/following-sibling::input")

password_input.send_keys('123456')

assert len(password_input.get_attribute("value")) > 5

time.sleep(5)
driver.quit()

