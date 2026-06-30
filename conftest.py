import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait


@pytest.fixture(scope="function") #Фикстура для создания и закрытия драйвера
def driver():
    driver = webdriver.Chrome()
    driver.get("https://qa-desk.education-services.ru/")
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.fixture(scope="function") #Фикстура для явных ожиданий
def wait(driver):
    return WebDriverWait(driver, 20)


@pytest.fixture(scope="function") #Генерация уникального пользователя для каждого теста
def random_user():
    import time
    timestamp = int(time.time())
    return {
        "email": f"user_{timestamp}_{timestamp}@test.ru",
        "password": "123456",
        "name": "User"
    }


@pytest.fixture(scope="function") #Генерация уникальных данных для объявления
def ad_data():
    import time
    timestamp = int(time.time())
    return {
        "title": f"Тестовое объявление {timestamp}",
        "description": "Описание тестового объявления",
        "price": "1000"
    }
