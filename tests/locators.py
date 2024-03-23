from selenium.webdriver.common.by import By

class TestLocators():
    # кнопка войти в аккаунт
    ENTER_TO_ACCOUNT_BUTTON = (By.XPATH, ".//*[text()='Войти в аккаунт']")
    # гипперссылка Регистрация
    REGISTRATION_LINK = (By.CLASS_NAME, "Auth_link__1fOlj")
    # поле ввода данных имени на странице регистрации
    INPUT_NAME = (By.XPATH, ".//*[text()='Имя']/following-sibling::input")
    # INPUT_NAME = driver.find_element(By.XPATH, "//label[text()='Имя']/following-sibling::input")
    # поле ввода email на странице регистрации
    INPUT_EMAIL = (By.XPATH, ".//*[text()='Email']/following-sibling::input")
    # поле ввода Пароль на странице регистрации
    INPUT_PASSWORD = (By.XPATH, ".//*[text()='Пароль']/following-sibling::input")
    # кнока "Зарегистрироваться" на странице регистрации
    REGISTRATION_BUTTON = (By.XPATH, ".//*[text()='Зарегистрироваться']")
    #поле ввода почты на странице входа
    INPUT_EMAIL_LOGIN = (By.XPATH, ".//*[text()='Email']/following-sibling::input")
    #поле ввода пароля
    INPUT_PASSWORD_LOGIN = (By.XPATH, ".//*[text()='Пароль']/following-sibling::input")
    #кнопка войти на странице ввода логина и пароля
    ENTER_BUTTON_LOGIN = (By.XPATH, ".//button[text()='Войти']")
    #кнопка оформить заказ
    CREATE_ORDER = (By.XPATH, ".//button[text() = 'Оформить заказ']")
    #сообщене об ошибке "некорректный пароль"
    FAILED_PASSWORD_TEXT =(By.XPATH, ".//form//p[text()='Некорректный пароль']")
    #кнопка Личный кабинет
    PERSONAL_ACCOUNT = ( By.XPATH, ".//p[text() = 'Личный Кабинет']")
     #гипперссылка Войти на странице регистрации
    ENTER_LINK = (By.XPATH, ".//a[text() = 'Войти']")
    #кнопка Восстановить пароль на странице ввода логина и пароля
    NEW_PASSWORD_LINK = (By.XPATH, ".//a[text() = 'Восстановить пароль']")
    #гипперссылка Войти на странице Восстановления пароля
    NEW_PASSWORD_ENTER_BUTTON = (By.XPATH, ".//a[text() = 'Войти']")
    #вкладка "Профиль" в личном кабинете
    PROFILE_TAB = (By.XPATH, ".//a[text()='Профиль']")
    #кнопка конструктор для перехода раздела оформления заказа
    CONSTRUCTOR_BUTTON = (By.XPATH, ".//p[text() = 'Конструктор']")
     #логотип Stellar Burgers для перехода из личного кабинета
    LOGO = (By.CLASS_NAME, 'AppHeader_header__logo__2D0X2')
     #кнопка Выйти в личном кабинете
    LOG_OUT_BUTTON = (By.XPATH, ".//button[text()='Выход']")
    #вкладка "Булки" в конструкторе
    BREAD_TAB = (By.XPATH, ".//span[text() = 'Булки']")
    #вкладка "Соусы" в конструкторе
    SOUSE_TAB = (By.XPATH, ".//span[text() = 'Соусы']")
    #вкладка "Начинки" в конструкторе
    FILLING_TAB = (By.XPATH, ".//span[text() = 'Начинки']")