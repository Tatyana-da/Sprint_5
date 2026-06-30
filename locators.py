from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_REGISTER_BUTTON = (By.XPATH, "//button[contains(text(), 'Вход и регистрация')]")
    CREATE_AD_BUTTON = (By.XPATH, "//button[contains(text(), 'Разместить объявление')]")


class AuthPageLocators:
    REGISTER_LINK = (By.XPATH, "//button[contains(text(), 'Нет аккаунта')]")
    LOGIN_EMAIL_INPUT = (By.XPATH, "//input[@name='email' and @placeholder='Введите Email']")
    LOGIN_PASSWORD_INPUT = (By.XPATH, "//input[@name='password' and @placeholder='Пароль']")
    EMAIL_INPUT = (By.XPATH, "//input[@name='email' and @placeholder='Введите Email']")
    PASSWORD_INPUT = (By.XPATH, "//input[@name='password' and @placeholder='Пароль']")
    CONFIRM_PASSWORD_INPUT = (By.XPATH, "//input[@name='submitPassword' and @placeholder='Повторите пароль']")
    NAME_INPUT = (By.XPATH, "//input[@name='name' and @placeholder='Я хочу купить...']")
    CREATE_ACCOUNT_BUTTON = (By.XPATH, "//button[contains(text(), 'Создать аккаунт')]")
    LOGIN_BUTTON = (By.XPATH, "//button[contains(text(), 'Войти')]")
    ERROR_MESSAGE = (By.XPATH, "//*[contains(text(), 'Ошибка')]")


class ProfilePageLocators:
    USER_NAME = (By.XPATH, "//h3[contains(@class, 'profileText') and contains(text(), 'User')]")
    LOGOUT_BUTTON = (By.XPATH, "//button[contains(text(), 'Выйти')]")
    MY_ADS_BLOCK = (By.XPATH, "//h1[text()='Мои объявления']")
    AD_TITLE = (By.XPATH, "//div[contains(@class, 'card')]//div[contains(@class, 'about')]//h2")


class AdPageLocators:
    TITLE_INPUT = (By.XPATH, "//input[@name='name' and @placeholder='Название']")
    DESCRIPTION_INPUT = (By.XPATH, "//textarea[@name='description' and @placeholder='Описание товара']")
    PRICE_INPUT = (By.XPATH, "//input[@name='price' and @placeholder='Стоимость']")
    CATEGORY_INPUT = (By.XPATH, "//*[@id='root']/div/div[2]/div/form/div[2]/div[2]/div[1]/button")
    CITY_INPUT = (By.XPATH, "//*[@id='root']/div/div[2]/div/form/div[3]/div[1]/button")
    RADIO_NEW = (By.XPATH, "//input[@type='radio' and @name='condition' and @value='Новый']/..")
    PUBLISH_BUTTON = (By.XPATH, "//button[contains(text(), 'Опубликовать')]")
    