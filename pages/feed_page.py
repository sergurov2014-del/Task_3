import allure
from pages.base_page import BasePage
from selenium.common.exceptions import TimeoutException
import locators.locators_feed_page as loc
from time import sleep
from urls import FEED_URL


class FeedPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver, FEED_URL)

    @allure.step("Кликаем на раздел 'История заказов'")
    def click_last_order(self):
        last_order = self.wait_for_elements(loc.ORDER_FEED_ITEMS_LINK)[0]
        self.click_button(last_order)

    @allure.step("Проверить, что открыто модальное окно с деталями заказа")
    def is_feed_modal_open(self):
        try:
            self.wait_until_element_located(loc.FEED_OVERLAY_MODAL_OPENED)
            return True
        except TimeoutException:
            return False

    @allure.step("Возвращаем текст окна заказы в работе")
    def return_text_orders_in_work(self):
        element = self.wait_until_element_located(loc.IN_WORK_ORDERS_LIST)
        return element.text

    @allure.step("Проверяем счётчик количества заказов за сегодня")
    def return_today_order_counter(self):
        element = self.is_element_visible(loc.TODAY_COMPLETED_COUNTER)
        counter = int(element.text)
        return counter

    @allure.step("Проверяем счётчик количества заказов за всё время")
    def return_all_orders_counter(self):
        element = self.is_element_visible(loc.TOTAL_COMPLETED_COUNTER)
        counter = int(element.text)
        return counter

    @allure.step("Ждём появления заказа в разделе 'В работе'")
    def wait_for_order_in_work(self, order_number):
        """Ждёт, пока в разделе 'В работе' появится указанный номер заказа."""
        try:
            self.wait_until_text_in_element(loc.FEED_OVERLAY_MODAL_OPENED, order_number)
            return True
        except TimeoutException:
            return False

    @allure.step("Получить номера заказов из ленты")
    def get_order_numbers_from_feed(self):
        items = self.wait_for_elements(loc.ORDER_FEED_ITEMS)
        numbers = []
        for item in items:
            number_el = item.find_element(*loc.ORDER_NUMBER_IN_FEED)
            number_str = number_el.text.strip("!@#№$%^&*()_ \\ / \n")
            number_normal = self.normalize(number_str)
            numbers.append(number_normal)
        return numbers

    @allure.step("Ждём появления заказов {order_numbers} в ленте")
    def wait_for_orders_in_feed(self, order_numbers):
        # 1. Сначала ждем появления КАЖДОГО заказа отдельно

        for num in order_numbers:
            try:
                self.wait.until(
                    lambda d, n=num: n in self.get_order_numbers_from_feed()
                )
            except TimeoutException:
                # Если какой-то один заказ не появился вообще — падаем сразу
                return False

            # 2. Небольшая пауза или дополнительная проверка, чтобы DOM точно "успокоился"
            # React постоянно перерисовывает страницу, не понятно чего именно ждать
            # тест проходил в firefox в chromt падал, чтобы это пофиксить используется
            # костыль в виде sleep(2),чтобы дать react всё прогрузить
            sleep(2)
            return True


    @allure.step("Ждём увеличения счётчика 'Выполнено за сегодня' с {previous}")
    def wait_for_today_counter_increase(self, previous, timeout=15):
        """Ждёт, пока счётчик 'за сегодня' станет > previous. Возвращает новое значение."""
        self.wait.until(
            lambda d: self.return_today_order_counter() > previous,
            message=f"Счётчик 'за сегодня' не увеличился с {previous} за {timeout} сек.",
        )
        return self.return_today_order_counter()

    @allure.step("Ждём увеличения счётчика 'Выполнено за всё время' с {previous}")
    def wait_for_all_time_counter_increase(self, previous, timeout=15):
        self.wait.until(
            lambda d: self.return_all_orders_counter() > previous,
            message=f"Счётчик 'за всё время' не увеличился с {previous} за {timeout} сек.",
        )
        return self.return_all_orders_counter()
