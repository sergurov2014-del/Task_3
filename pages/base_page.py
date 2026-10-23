import allure
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:  # Базовые методы взаимодействия с любыми страницами

    def __init__(self, driver, url=""):
        self.driver = driver
        self.url = url
        self.wait = WebDriverWait(driver, 10)  # Стандартное время ожидания

    #######################НАЖАТИЕ НА КНОПКИ ########################################################

    @allure.step("Нажимаем на кнопку c локатором {button_locator}")
    def click_button(self, button_locator):  # ожидаем доступности и кликаем на кнопку
        element = self.wait.until(EC.element_to_be_clickable(button_locator))
        element.click()

    def js_click(self, locator):  # клик по локатору с ожидаением
        element = self.wait.until(EC.presence_of_element_located(locator))
        self.driver.execute_script("arguments[0].click();", element)

    def js_click_element(self, element):  # клик по элементу без ожидания
        self.driver.execute_script("arguments[0].click();", element)

    #######################ПОИСК########################################################

    @allure.step("Ищем и возвращаем элемент c локатором {locator}")
    def find_element(self, locator):  # метод ищет элемент и возвращает его
        return self.driver.find_element(*locator)

    @allure.step("Ищем и возвращаем список элементов по локатору {locator}")
    def find_elements(self, locator):  # метод ищет элемент и возвращает его
        return self.driver.find_elements(*locator)

    @allure.step("Находим элемент c локатором {locator} и вводим туда {data}")
    def send_keys(self, locator, data):  # ожидаем доступности, чистим, потом вводим
        element = self.wait.until(EC.element_to_be_clickable(locator))
        element.clear()
        element.send_keys(data)
        return element

    @allure.step("Возврашаем элемент c локатором {locator}")
    def get_text(self, locator):
        return self.find_element(locator).text

    #######################РАБОТА С ВРЕМЕНЕМ ОЖИДАНИЯ########################################################

    @allure.step(
        "Ждём пока элемент c локатором {button_locator} станет видимым (до 5 сек.)"
    )
    def wait_until_element_located(self, button_locator):
        return self.wait.until(EC.visibility_of_element_located(button_locator))

    @allure.step(
        "Ждём пока элемент c локатором {button_locator} станет кликабельным (до 5 сек.)"
    )
    def wait_until_element_is_clickable(self, button_locator):
        return self.wait.until(EC.element_to_be_clickable(button_locator))

    @allure.step(
        "Ждём пока элемент c локатором {button_locator} станен невидимым(до 5 сек.)"
    )
    def wait_for_element_not_visible(self, button_locator):
        """Ожидает, пока элемент станет невидимым."""
        return self.wait.until_not(EC.visibility_of_element_located(button_locator))

    #######################РАБОТА С URL########################################################

    def open(self):  # Открывает страницу по URL
        with allure.step(f"Открыть страницу {self.url}"):
            self.driver.get(self.url)
        return self

    @allure.step("Возвращает текущий URL браузера.")
    def get_current_url(self):
        return self.driver.current_url

    @allure.step("Проверяем, что текущий URL равен '{expected_url}'")
    def is_url_equals(self, expected_url):
        return self.driver.current_url == expected_url

    @allure.step("Проверяем, что текущий URL содержит '{expected_url}'")
    def is_url_contains(self, expected_url):
        return expected_url in self.driver.current_url

    @allure.step("Ожидаем 5 сек,того что текущий URL содержит '{expected_url}'")
    def wait_for_url_contains(self, expected_url):
        """Ожидает, пока URL не будет содержать указанную подстроку."""
        self.wait.until(EC.url_contains(expected_url))

    def wait_for_url_not_contains(self, url_fragment):
        """Ожидает, пока URL перестанет содержать указанную подстроку."""
        self.wait.until_not(EC.url_contains(url_fragment))

    @allure.step("Получаем атрибут '{attribute}' у элемента с локатором {locator}")
    def get_element_attribute(self, locator, attribute):
        element = self.wait.until(EC.presence_of_element_located(locator))
        return element.get_attribute(attribute)

    def is_element_visible(self, locator):
        # ждёт один элемент и возвращает один WebElement (первый найденный)
        return self.wait.until(EC.visibility_of_element_located(locator))

    def wait_for_elements(self, locator):
        # Ждёт появления элементов по локатору и возвращает список WebElement
        return self.wait.until(EC.presence_of_all_elements_located(locator))

    def wait_until_text_in_element(self, locator, text):
        return self.wait.until(EC.text_to_be_present_in_element(locator, text))

    def normalize(self, number):
        return str(int(number))
