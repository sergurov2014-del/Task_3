from pages.base_page import BasePage
import allure
from urls import RECOVER_PASS_URL
import locators.locators_recover_pass_page as loc
import helpers


class RecoveryPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver, RECOVER_PASS_URL)

    @allure.step("Вводим email")
    def enter_email(self):
        email = helpers.get_random_email()
        self.send_keys(loc.EMAIL_INPUT, email)

    @allure.step("Кликаем на кнопку 'Восстановить'")
    def click_recover_button(self):
        self.js_click(loc.RECOVER_BUTTON)

    @allure.step("Вводим password")
    def enter_password(self):
        password = helpers.get_random_password()

        self.send_keys(loc.PASSWORD_INPUT, password)
        

    @allure.step("Кликаем на кнопку 'Сохранить'")
    def click_save_button(self):
        self.js_click(loc.SAVE_BUTTON)

    @allure.step("Кликаем на иконку глаза - скрыть/открыть пароль")
    def toggle_password_visibility(self):
        self.js_click(loc.PASSWORD_EYE_TOGGLE)

    @allure.step("Кликаем на кнопку 'Войти'")
    def click_enter_button(self):
        self.js_click(loc.ENTER_LINK)

    @allure.step("Проверить, что открыта страница восстановления пароля")
    def is_forgot_password_page(self):
        self.wait_for_url_contains("/forgot-password")
        return "/forgot-password" in self.get_current_url()

    @allure.step("Проверить, что открыта страница установки нового пароля")
    def is_reset_password_page(self):
        self.wait_for_url_contains("/reset-password")
        return "/reset-password" in self.get_current_url()

    @allure.step("Проверить тип поля пароля")
    def get_password_input_type(self):
        return self.get_element_attribute(loc.PASSWORD_INPUT, "type")
    
    @allure.step("Проверить, что поле пароля активно (подсвечено)")
    def is_password_field_active(self): # True, если поле пароля подсвечено = активный стиль
        return self.is_element_visible(loc.PASSWORD_CONTAINER_ACTIVATED)
