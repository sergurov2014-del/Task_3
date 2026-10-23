import pytest
from urls import BASE_URL
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from pages.login_page import LoginPage
import helpers


# scope="function" Область жизни фикстуры — одна тестовая функция.
# params=["chrome", "firefox"] -прогоны будут сразу в двух браузерах Chrome и Firefox
# Создаёт WebDriver для Chrome/Firefox, открывает BASE_URL, закрывает после теста.
@pytest.fixture(params=["chrome", "firefox"], scope="function")
def driver(request):
    if request.param == "chrome":
        options = ChromeOptions()
        options.add_argument("--start-maximized")
        options.add_argument("--disable-notifications")
        driver = webdriver.Chrome(options=options)
    elif request.param == "firefox":
        options = FirefoxOptions()
        options.set_preference("signon.rememberSignons", False)
        options.set_preference("dom.webnotifications.enabled", False)
        driver = webdriver.Firefox(options=options)
        driver.maximize_window()

    driver.get(BASE_URL)
    yield driver
    driver.quit()


@pytest.fixture
def authorized_user_driver(driver):

    login_page = LoginPage(driver)

    email, password, name = helpers.register_user()
    login_page.open()
    login_page.enter_email(email)
    login_page.enter_password(password)
    login_page.click_enter_button()
    login_page.wait_for_url_not_contains("/login")

    return driver
