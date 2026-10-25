import allure
from pages.main_page import MainPage
from pages.feed_page import FeedPage
from pages.account_page import AccountPage
import helpers


@allure.feature("Лента заказов")
class TestOrderFeed:

    @allure.title("Переход по клику на 'Лента заказов'")
    def test_navigate_to_order_feed(self, driver):
        feed_page = FeedPage(driver)
        feed_page.open()
        feed_page.click_last_order()

        assert feed_page.is_feed_modal_open(), "Модальное окно не открылось"

    @allure.title("Заказы попадают в раздел «История заказов»")
    def test_new_orders_visible_in_orders_history_(
        self,
        authorized_user_driver,
        make_two_different_orders,
    ):
        order_number1, order_number2 = make_two_different_orders

        main_page = MainPage(authorized_user_driver)
        main_page.open()
        main_page.go_to_login_page_via_personal_account()

        account_page = AccountPage(authorized_user_driver)
        account_page.click_order_history_button()
        history_order_numbers = account_page.return_order_numbers_from_history()

        assert (
            order_number1 in history_order_numbers
        ), f"Заказ {order_number1} не найден в истории: {history_order_numbers}"
        assert (
            order_number2 in history_order_numbers
        ), f"Заказ {order_number2} не найден в истории: {history_order_numbers}"

    @allure.title(
        "Заказы из раздела История заказов» отображаются на странице «Лента заказов»"
    )
    def test_orders_from_orders_history_visible_in_order_feed(
        self,
        authorized_user_driver,
        make_two_different_orders,
    ):
        order_number1, order_number2 = make_two_different_orders

        main_page = MainPage(authorized_user_driver)
        main_page.open()
        main_page.go_to_login_page_via_personal_account()

        account_page = AccountPage(authorized_user_driver)
        account_page.click_order_history_button()
        history_order_numbers = account_page.return_order_numbers_from_history()
        feed_page = FeedPage(authorized_user_driver)
        feed_page.open()
        feed_page.wait_for_orders_in_feed([order_number1, order_number2])
        feed_numbers = feed_page.get_order_numbers_from_feed()
        assert (
            order_number1 in feed_numbers
        ), f"Заказ {order_number1} не найден в ленте: {feed_numbers}"
        assert (
            order_number2 in feed_numbers
        ), f"Заказ {order_number2} не найден в ленте: {feed_numbers}"

    @allure.title("Создание нового заказа увеличивает счётчик Выполнено за сегодня")
    def test_today_order_counter_increases(self, authorized_user_driver):
        feed_page = FeedPage(authorized_user_driver)
        feed_page.open()
        counter_before = feed_page.return_today_order_counter()
        helpers.make_new_order(authorized_user_driver)
        feed_page.open()
        counter_after = feed_page.wait_for_today_counter_increase(counter_before)

        assert (
            counter_after > counter_before
        ), f"Счётчик не увеличился за 15 секунд. Было: {counter_before}"

    @allure.title("Создание нового заказа увеличит счётчик Выполнено за всё время")
    def test_all_time_orders_counter_increases(self, authorized_user_driver):
        feed_page = FeedPage(authorized_user_driver)
        feed_page.open()
        counter_before = feed_page.return_all_orders_counter()
        helpers.make_new_order(authorized_user_driver)
        feed_page.open()
        counter_after_order = feed_page.wait_for_all_time_counter_increase(
            counter_before
        )

        assert (
            counter_before < counter_after_order
        ), "Количество заказов за сегодня не изменилось или изменилось больше чем на 1"

    @allure.title("Номер созданного заказа появляется в разделе в работе")
    def test_created_order_number_appears_in_work_section(self, authorized_user_driver):
        feed_page = FeedPage(authorized_user_driver)
        feed_page.open()
        text_befor_order = feed_page.return_text_orders_in_work()
        order_number = helpers.make_new_order(authorized_user_driver)
        feed_page.open()
        feed_page.wait_for_order_in_work(order_number)
        text_after_order = feed_page.return_text_orders_in_work()
        assert (
            order_number in text_after_order
        ), "Номер заказа не воявляется в тексте после заказа"
