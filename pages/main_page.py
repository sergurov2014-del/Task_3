import allure
from pages.base_page import BasePage
from selenium.common.exceptions import TimeoutException
from urls import BASE_URL
import locators.locators_main_page as loc


class MainPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver, BASE_URL)

    @allure.step("Переходим на страницу логина, через кнопку 'Войти в аккаунт'")
    def go_to_login_page_via_enter_button(self):
        self.js_click(loc.LOGIN_BUTTON)

    @allure.step("Переходим на страницу логина,через кнопку 'Личный кабинет'")
    def go_to_login_page_via_personal_account(self):
        self.js_click(loc.PERSONAL_ACCOUNT_LINK)

    @allure.step("Переходим в 'Ленту заказов'")
    def go_to_order_feed(self):

        element = self.wait_until_element_is_clickable(loc.ORDER_FEED_BUTTON)
        self.js_click(loc.ORDER_FEED_BUTTON)  #

    @allure.step("Переходим в 'Конструктор'")
    def go_to_constructor(self):
        self.js_click(loc.CONSTRUCTOR_BUTTON)

    @allure.step("Проверяем, что url содержит '/feed'")
    def is_url_contains_feed(self):
        return self.is_url_contains("/feed")

    @allure.step("Проверить, что открыто модальное окно с деталями ингредиента")
    def is_ingredient_modal_open(self):
        return self.wait_until_element_located(loc.INGREDIENT_INFORMATION_MODAL_WINDOW)

    @allure.step("Закрыть модальное окно по крестику")
    def close_modal_window(self):
        self.js_click(loc.CLOSE_MODAL_WINDOW_BUTTON)

    @allure.step("Проверить, что модальное окно закрыто")
    def is_modal_closed(self):
        """Ожидает закрытия модального окна и возвращает True, если оно не отображается."""
        self.wait_for_element_not_visible(loc.INGREDIENT_INFORMATION_MODAL_WINDOW)
        return True

    @allure.step("Проверить, что открыта главная страница")
    def is_main_page(self):
        return self.get_current_url() == BASE_URL

    @allure.step("Кликаем на кнопку 'Оформить заказ'")
    def click_button_make_order(self):
        self.js_click(loc.CREATE_ORDER_BUTTON)

    @allure.step("Кликаем на ингредиент с индексом {index}")
    def click_ingredient(self, index=0):
        try:
            ingredients = self.wait_for_elements(loc.ALL_INGEDIENT_CARDS)
        except TimeoutException:
            raise AssertionError("Ингредиенты не загрузились за 5 секунд")

        if not ingredients or len(ingredients) <= index:
            raise AssertionError(
                f"Нет ингредиента с индексом {index}: найдено {len(ingredients)}"
            )
        self.scroll_into_view(ingredients[index])
        self.js_click_element(ingredients[index])

    @allure.step("Перетащить ингредиент с индексом {index} в конструктор")
    def drag_and_drop_ingredient_to_constructor(self, index=0):
        try:
            ingredients = self.wait_for_elements(loc.ALL_INGEDIENT_CARDS)
        except TimeoutException:
            raise AssertionError("Ингредиенты не загрузились за 5 секунд")

        if index < 0 or not ingredients or len(ingredients) <= index:
            raise AssertionError(
                f"Нет ингредиента с индексом {index}: найдено {len(ingredients)}"
            )

        element = ingredients[index]

        self.scroll_into_view(element)

        target = self.wait_until_element_located(loc.CONSTRUCTOR_BASKET)
        self.scroll_into_view(target)
        self.js_for_drag_and_drop(element, target)

    @allure.step("Получить счётчик ингредиента с индексом {index}")
    def get_ingredient_counter(self, index=0):
        # Возвращает текст счётчика внутри карточки ингредиента с указанным индексом.
        # Если счётчика нет (ингредиент ещё не добавляли) — возвращает '0'.
        try:
            ingredients = self.wait_for_elements(loc.ALL_INGEDIENT_CARDS)
        except TimeoutException:
            raise AssertionError("Ингредиенты не загрузились за 10 секунд")

        if index < 0 or not ingredients or len(ingredients) <= index:
            raise AssertionError(
                f"Нет ингредиента с индексом {index}: найдено {len(ingredients)}"
            )

        ingredient = ingredients[index]
        counters = ingredient.find_elements(*loc.CARDS_COUNTER)
        return counters[0].text if counters else "0"

    @allure.step("Получить номер готовящегося заказа")
    def return_cooking_order_number(self):
        try:
            element = self.is_element_visible(
                loc.FIELD_WITH_NUMBER_OF_ORDER_IDENTIFICATOR
            )
            self.wait.until(
                lambda d: element.text.strip() != "9999"
            )  # 9999 значение по умолчанию, chrome считывает его до того как реакт подгрузит номер заказа
            return element.text.strip()
        except TimeoutException:
            raise AssertionError("Номер заказа не загрузился за 5 секунд")
