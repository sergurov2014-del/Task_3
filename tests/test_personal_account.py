import allure
from pages.main_page import MainPage
from pages.account_page import AccountPage


@allure.feature("Личный кабинет")
class TestPersonalAccount:

    @allure.title("Переход по кнопке «Личный кабинет»")
    def test_go_to_personal_account_from_main(self, authorized_user_driver):
        main_page = MainPage(authorized_user_driver)
        main_page.go_to_login_page_via_personal_account()

        account_page = AccountPage(authorized_user_driver)
        account_page.wait_for_account_page_load()
        assert account_page.is_account_page(), "Страница личного кабинета не открылась"

    @allure.title("Проверка перехода в раздел «История заказов»")
    def test_go_to_orders_history(self, authorized_user_driver):
        main_page = MainPage(authorized_user_driver)
        main_page.go_to_login_page_via_personal_account()

        account_page = AccountPage(authorized_user_driver)
        account_page.wait_for_account_page_load()
        account_page.click_order_history_button()
        assert (
            account_page.is_order_history_page()
        ), "Страница «История заказов» не открылась"

    @allure.title("Проверка выхода из аккаунта")
    def test_exit_accout(self, authorized_user_driver):
        main_page = MainPage(authorized_user_driver)
        main_page.go_to_login_page_via_personal_account()

        account_page = AccountPage(authorized_user_driver)
        account_page.wait_for_account_page_load()
        account_page.click_exit_button()
        assert account_page.is_redirected_to_login(), "Не получилось выйти из аккаунта"