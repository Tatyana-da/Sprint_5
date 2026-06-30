import pytest
from selenium.webdriver.support import expected_conditions as EC
from locators import MainPageLocators, AuthPageLocators, ProfilePageLocators


class TestLogout: #Класс для тестов выхода из системы    
    #Выход из системы
    def test_logout_success(self, driver, wait, random_user):
        # Шаг 1: Сначала регистрируем пользователя
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

        # Проверяем, что пользователь создан и авторизован
        wait.until(EC.visibility_of_element_located(ProfilePageLocators.USER_NAME))

        # Шаг 2: Нажимаем на кнопку «Выйти»
        wait.until(EC.presence_of_element_located(ProfilePageLocators.LOGOUT_BUTTON))
        driver.find_element(*ProfilePageLocators.LOGOUT_BUTTON).click()

        # Шаг 3: Проверяем, что появилась кнопка «Вход и регистрация»
        wait.until(EC.visibility_of_element_located(MainPageLocators.LOGIN_REGISTER_BUTTON))
        login_button = driver.find_element(*MainPageLocators.LOGIN_REGISTER_BUTTON)

        assert login_button.is_displayed()
