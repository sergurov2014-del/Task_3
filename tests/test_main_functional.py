import allure
from pages.main_page import MainPage
import helpers


@allure.feature("Основной функционал")
class TestMainFunctional:

    @allure.title("Переход по клику на 'Лента заказов'")
    def test_navigate_to_order_feed(self, driver):
        main_page = MainPage(driver)
        main_page.open()
        main_page.go_to_order_feed()
        main_page.wait_for_url_contains("/feed")
        assert main_page.is_url_contains_feed()

    @allure.title("Переход по клику на «Конструктор»")
    def test_navigate_to_constructor(self, driver):
        main_page = MainPage(driver)
        main_page.open()
        main_page.go_to_order_feed()
        main_page.wait_for_url_contains("/feed")
        main_page.go_to_constructor()
        main_page.wait_for_url_not_contains("/feed")
        assert not main_page.is_url_contains_feed()

    @allure.title("Появление всплывающего окна при клике на ингридиент")
    def test_ingedient_modal_opens_on_click(self, driver):
        main_page = MainPage(driver)
        main_page.open()
        main_page.click_ingredient()
        assert (
            main_page.is_ingredient_modal_open()
        ), "Всплывающее окно при клике на ингридиент не появилось"

    @allure.title("Закрытие всплывающего окна при клике на крестик")
    def test_ingedient_modal_closes_on_cross_click(self, driver):
        main_page = MainPage(driver)
        main_page.open()
        main_page.click_ingredient()
        main_page.close_modal_window()
        assert main_page.is_modal_closed()

    @allure.title(
        "При добавлении ингридиента в заказ, увеличивается каунтер этого ингредиента"
    )
    def test_adding_ingedient_increments_ingredient_counter(self, driver):
        main_page = MainPage(driver)
        main_page.open()
        index = 0
        counter_before = main_page.get_ingredient_counter(index)
        main_page.drag_and_drop_ingredient_to_constructor(index)
        # ждём, пока React обновит счётчик (до 5 сек.)
        main_page.wait.until(
            lambda d: main_page.get_ingredient_counter(index) != counter_before
        )
        counter_after = main_page.get_ingredient_counter(index)
        assert int(counter_after) > int(counter_before), (
            f"Счётчик ингредиента {index} не увеличился: "
            f"было {counter_before}, стало {counter_after}"
        )

    @allure.title("залогиненный пользователь может оформить заказ")
    def test_autorized_user_can_create_order(self, authorized_user_driver):
        order_number = helpers.make_new_order(authorized_user_driver)
        assert order_number.isdigit(), f"Номер заказа не число: {order_number!r}"
        assert (
            1 <= int(order_number) <= 9999
        ), f"Номер заказа вне разумного диапазона: {order_number}"
