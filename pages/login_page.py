from pages.base_page import BasePage
import allure
from urls import LOGIN_URL
import locators.locators_login_page as loc


class LoginPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver, LOGIN_URL)

    @allure.step("Вводим email: {email}")
    def enter_email(self, email):
        self.send_keys(loc.EMAIL_INPUT, email)

    @allure.step("Вводим password: {password}")
    def enter_password(self, password):
        self.send_keys(loc.PASSWORD_INPUT, password)

    @allure.step("Кликаем на кнопку 'Войти'")
    def click_enter_button(self):
        self.js_click(loc.ENTER_BUTTON)

    @allure.step("Кликаем на поле 'Зарегистрироваться'")
    def click_registration_field(self):
        self.js_click(loc.REGISTER_LINK)

    @allure.step("Кликаем на поле 'Восстановить пароль'")
    def click_recover_password_field(self):
        self.js_click(loc.RECOVERY_LINK)

    @allure.step("Кликаем на иконку глаза - скрыть/открыть пароль")
    def toggle_password_visibility(self):
        self.js_click(loc.PASSWORD_EYE_TOGGLE)
