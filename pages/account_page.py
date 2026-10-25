from pages.base_page import BasePage
import allure
from urls import ACCOUNT_URL
import locators.locators_account_page as loc


class AccountPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver, ACCOUNT_URL)

    @allure.step("Кликаем на раздел 'История заказов'")
    def click_order_history_button(self):
        self.js_click(loc.ORDER_HISTORY_BUTTON)

    @allure.step("Кликаем на кнопку 'Выход'")
    def click_exit_button(self):
        self.js_click(loc.EXIT_BUTTON)

    @allure.step("После выхода проверяем, что открыта страница входа ")
    def is_redirected_to_login(self):
        # Ждём 5 сек, возвращаем True, если произошёл редирект на страницу логина
        self.wait_for_url_contains("/login")
        return "/login" in self.get_current_url()

    @allure.step("Дождаться загрузки страницы личного кабинета")
    def wait_for_account_page_load(self):
        self.wait_for_url_contains("/account/profile")

    @allure.step("Проверить, что открыта страница личного кабинета")
    def is_account_page(self):
        return "/account/profile" in self.get_current_url()

    @allure.step("Проверить, что открыта страница истории заказов")
    def is_order_history_page(self):
        return "/account/order-history" in self.get_current_url()

    @allure.step("Получить номера заказов из истории заказов")
    def return_order_numbers_from_history(self):
        items=self.wait_for_elements(loc.ORDER_HISTORY_ITEMS)
        order_numbers=[]
        for item in items:
            number_el = item.find_element(*loc.ORDER_NUMBER_IN_HISTORY)
            number_str = number_el.text.strip("!@#№$%^&*()_ \\ / \n")
            number_normal = self.normalize(number_str)
            order_numbers.append(number_normal)
        
        return order_numbers
