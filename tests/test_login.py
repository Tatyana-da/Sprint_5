import pytest
from selenium.webdriver.support import expected_conditions as EC
from locators import MainPageLocators, AuthPageLocators, ProfilePageLocators


class TestLogin: #Класс для тестов авторизации
    #Вход зарегистрированного пользователя
    def test_login_success(self, driver, wait, random_user):
        # Шаг 1: Регистрируем пользователя
        wait.until(EC.presence_of_element_located(MainPageLocators.LOGIN_REGISTER_BUTTON))
        driver.find_element(*MainPageLocators.LOGIN_REGISTER_BUTTON).click()

        wait.until(EC.presence_of_element_located(AuthPageLocators.REGISTER_LINK))
        driver.find_element(*AuthPageLocators.REGISTER_LINK).click()

        wait.until(EC.visibility_of_element_located(AuthPageLocators.EMAIL_INPUT)).send_keys(random_user["email"])
        driver.find_element(*AuthPageLocators.PASSWORD_INPUT).send_keys(random_user["password"])
        driver.find_element(*AuthPageLocators.CONFIRM_PASSWORD_INPUT).send_keys(random_user["password"])
        driver.find_element(*AuthPageLocators.NAME_INPUT).send_keys(random_user["name"])

        wait.until(EC.presence_of_element_located(AuthPageLocators.CREATE_ACCOUNT_BUTTON))
        driver.find_element(*AuthPageLocators.CREATE_ACCOUNT_BUTTON).click()

        # Проверяем, что пользователь создан
        wait.until(EC.visibility_of_element_located(ProfilePageLocators.USER_NAME))

        # Шаг 2: Выходим из системы
        wait.until(EC.presence_of_element_located(ProfilePageLocators.LOGOUT_BUTTON))
        driver.find_element(*ProfilePageLocators.LOGOUT_BUTTON).click()
        wait.until(EC.visibility_of_element_located(MainPageLocators.LOGIN_REGISTER_BUTTON))

        # Шаг 3: Нажать кнопку «Вход и регистрация»
        wait.until(EC.presence_of_element_located(MainPageLocators.LOGIN_REGISTER_BUTTON))
        driver.find_element(*MainPageLocators.LOGIN_REGISTER_BUTTON).click()

        # Шаг 4: Заполнить поля формы авторизации
        wait.until(EC.visibility_of_element_located(AuthPageLocators.LOGIN_EMAIL_INPUT)).send_keys(random_user["email"])
        driver.find_element(*AuthPageLocators.LOGIN_PASSWORD_INPUT).send_keys(random_user["password"])

        # Шаг 5: Нажать кнопку «Войти»
        wait.until(EC.presence_of_element_located(AuthPageLocators.LOGIN_BUTTON))
        driver.find_element(*AuthPageLocators.LOGIN_BUTTON).click()

        # Шаг 6: Проверить, что отображается имя User
        wait.until(EC.visibility_of_element_located(ProfilePageLocators.USER_NAME))
        user_name = driver.find_element(*ProfilePageLocators.USER_NAME)

        assert "User" in user_name.text
