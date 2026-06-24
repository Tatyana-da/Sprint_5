import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait


@pytest.fixture(scope="function")
def driver():
    """Фикстура для создания и закрытия драйвера."""
    driver = webdriver.Chrome()
    driver.get("https://qa-desk.education-services.ru/")
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.fixture(scope="function")
def wait(driver):
    """Фикстура для явных ожиданий."""
    return WebDriverWait(driver, 20)


@pytest.fixture(scope="function")
def random_user():
    """Генерация уникального пользователя для каждого теста."""
    import time
    timestamp = int(time.time())
    return {
        "email": f"user_{timestamp}_{timestamp}@test.ru",
        "password": "123456",
        "name": "User"
    }


@pytest.fixture(scope="function")
def ad_data():
    """Генерация уникальных данных для объявления."""
    import time
    timestamp = int(time.time())
    return {
        "title": f"Тестовое объявление {timestamp}",
        "description": "Описание тестового объявления",
        "price": "1000"
    }
