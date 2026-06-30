import pytest
from selenium.webdriver.support import expected_conditions as EC
from locators import MainPageLocators, AuthPageLocators, ProfilePageLocators


class TestRegistration:
    #Регистрация нового пользователя с корректными данными
    def test_registration_success(self, driver, wait, random_user):
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

        # После регистрации ищем имя пользователя заново
        wait.until(EC.visibility_of_element_located(ProfilePageLocators.USER_NAME))
        user_name = driver.find_element(*ProfilePageLocators.USER_NAME)

        assert "User" in user_name.text

    #Регистрация с email не по маске
    def test_registration_invalid_email(self, driver, wait):
        wait.until(EC.presence_of_element_located(MainPageLocators.LOGIN_REGISTER_BUTTON))
        driver.find_element(*MainPageLocators.LOGIN_REGISTER_BUTTON).click()

        wait.until(EC.presence_of_element_located(AuthPageLocators.REGISTER_LINK))
        driver.find_element(*AuthPageLocators.REGISTER_LINK).click()

        wait.until(EC.visibility_of_element_located(AuthPageLocators.EMAIL_INPUT)).send_keys("invalid_email")

        wait.until(EC.presence_of_element_located(AuthPageLocators.CREATE_ACCOUNT_BUTTON))
        driver.find_element(*AuthPageLocators.CREATE_ACCOUNT_BUTTON).click()

        wait.until(EC.visibility_of_element_located(AuthPageLocators.ERROR_MESSAGE))
        error_message = driver.find_element(*AuthPageLocators.ERROR_MESSAGE)

        assert error_message.text == "Ошибка"

    #Регистрация уже существующего пользователя
    def test_registration_existing_user(self, driver, wait, random_user):
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

        wait.until(EC.visibility_of_element_located(ProfilePageLocators.USER_NAME))

        wait.until(EC.presence_of_element_located(ProfilePageLocators.LOGOUT_BUTTON))
        driver.find_element(*ProfilePageLocators.LOGOUT_BUTTON).click()
        wait.until(EC.visibility_of_element_located(MainPageLocators.LOGIN_REGISTER_BUTTON))

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

        wait.until(EC.visibility_of_element_located(AuthPageLocators.ERROR_MESSAGE))
        error_message = driver.find_element(*AuthPageLocators.ERROR_MESSAGE)

        assert error_message.text == "Ошибка"
