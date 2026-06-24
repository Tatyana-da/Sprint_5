import pytest
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from locators import MainPageLocators, AuthPageLocators, ProfilePageLocators, AdPageLocators


class TestCreateAd: #Класс для тестов создания объявлений

    #Создание объявления неавторизованным пользователем
    def test_create_ad_unauthorized(self, driver, wait):
        wait.until(EC.presence_of_element_located(MainPageLocators.CREATE_AD_BUTTON))
        driver.find_element(*MainPageLocators.CREATE_AD_BUTTON).click()

        wait.until(EC.visibility_of_element_located(AuthPageLocators.LOGIN_EMAIL_INPUT))
        assert "login" in driver.current_url.lower()

    #Создание объявления авторизованным пользователем
    def test_create_ad_authorized(self, driver, wait, random_user, ad_data):
    
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

        wait.until(EC.visibility_of_element_located(ProfilePageLocators.USER_NAME))

        # Шаг 2: Нажимаем кнопку «Разместить объявление»
        wait.until(EC.presence_of_element_located(MainPageLocators.CREATE_AD_BUTTON))
        driver.find_element(*MainPageLocators.CREATE_AD_BUTTON).click()

        # Проверяем, что перешли на страницу создания объявления
        wait.until(EC.visibility_of_element_located(AdPageLocators.TITLE_INPUT))

        # Шаг 3: Заполняем все поля формы
        driver.find_element(*AdPageLocators.TITLE_INPUT).send_keys(ad_data["title"])
        driver.find_element(*AdPageLocators.DESCRIPTION_INPUT).send_keys(ad_data["description"])
        driver.find_element(*AdPageLocators.PRICE_INPUT).send_keys(ad_data["price"])

        # Шаг 4: Выбраем категорию
        category_input = driver.find_element(*AdPageLocators.CATEGORY_INPUT)
        category_input.click()
        time.sleep(0.5)
        
        # Ждём появления опций и кликаем по "Авто"
        category_option = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(@class, 'dropDownMenu_btn')]//span[text()='Авто']")))
        category_option.click()
        time.sleep(0.5)

        # Шаг 5: Выбраем город
        city_input = driver.find_element(*AdPageLocators.CITY_INPUT)
        city_input.click()
        time.sleep(0.5)
        
        # Ждём появления опций и кликаем по "Москва"
        city_option = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(@class, 'dropDownMenu_btn')]//span[text()='Москва']")))
        city_option.click()
        time.sleep(0.5)

        # Шаг 6: Выбираем RadioButton «Новый»
        driver.find_element(*AdPageLocators.RADIO_NEW).click()

        # Шаг 7: Нажимаем на кнопку «Опубликовать»
        wait.until(EC.presence_of_element_located(AdPageLocators.PUBLISH_BUTTON))
        driver.find_element(*AdPageLocators.PUBLISH_BUTTON).click()

        time.sleep(5)

        # Шаг 8: Переходим в профиль через URL
        driver.get("https://qa-desk.education-services.ru/profile")
        time.sleep(3)

        # Шаг 9: Проверяем объявление
        wait.until(EC.visibility_of_element_located(ProfilePageLocators.MY_ADS_BLOCK))
        ad_titles = driver.find_elements(*ProfilePageLocators.AD_TITLE)
        
        assert ad_data["title"] in ad_titles[-1].text
