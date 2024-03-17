#кнопка войти в аккаунт
driver.find_element(By.XPATH, ".//button[text()='Войти в аккаунт']")

#гипперссылка Регистрация
driver.find_element(By.CLASS_NAME, "Auth_link__1fOlj")

#поле ввода имя. При попытке указать индек элемента input, чтобы явно выбрать первый элемент input с плейсхолдером Имя,
# xpatch  в терминале браузера выдавал 3 элемента
#указал условие, при котором, нашел элемент с плейсхолером Имя и элемент после него
driver.find_element(By.XPATH, "//label[text()='Имя']/following-sibling::input")


#поле ввода email на странице регистрации
driver.find_element(By.XPATH, "//label[text()='Email']/following-sibling::input")

#поле ввода Пароль на странице регистрации
driver.find_element(By.XPATH, "//label[text()='Пароль']/following-sibling::input").click()


#кнокп "Зарегистрироваться" на странице регистрации
river.find_element(By.XPATH, ".//form//button[text()='Зарегистрироваться']")


#кнопка войти на странице ввода логина и пароля
driver.find_element(By.XPATH, ".//button[text()='Войти']")

#кнопка Личный кабинет
driver.find_element( By.XPATH, ".//p[text() = 'Личный Кабинет']")

#гипперссылка Войти на странице регистрации
driver.find_element(By.XPATH, ".//a[text() = 'Войти']")


#кнопка Восстановить пароль на странице ввода логина и пароля
driver.find_element(By.XPATH, ".//a[text() = 'Восстановить пароль']")

#гипперссылка Войти на странице Восстановления пароля
driver.find_element(By.XPATH, ".//a[text() = 'Войти']")пше

#кнопка конструктор для перехода раздела оформления заказа
driver.find_element(By.XPATH, ".//p[text() = 'Конструктор']")

#логотип Stellar Burgers
driver.find_element(By.CLASS_NAME, 'AppHeader_header__logo__2D0X2')

#кнопка Выйти в личном кабинете
driver.find_element(By.XPATH, ".//button[text()='Выход']")

#вкладка "Булки" в конструкторе
driver.find_element(By.XPATH, ".//span[text() = 'Булки']")

#вкладка "Соусы" в конструкторе
driver.find_element(By.XPATH, ".//span[text() = 'Соусы']")

#вкладка "Начинки" в конструкторе
driver.find_element(By.XPATH, ".//span[text() = 'Начинки']")