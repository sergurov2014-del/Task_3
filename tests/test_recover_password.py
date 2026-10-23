import allure
from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.recover_password_page import RecoveryPage


@allure.feature("Восстановление пароля")
class TestRecoverPassword:

    @allure.title(
        "Переход на страницу восстановления пароля по кнопке «Восстановить пароль»"
    )
    def test_go_to_recover_password_page(self, driver):
        main_page = MainPage(driver)
        main_page.go_to_login_page_via_personal_account()

        login_page = LoginPage(driver)
        login_page.click_recover_password_field()

        recovery_page = RecoveryPage(driver)
        assert (
            recovery_page.is_forgot_password_page()
        ), "Не выполнен переход на страницу сброса пароля"

    @allure.title("Ввод почты и клик по кнопке «Восстановить»")
    def test_enter_email_and_click_restore_button(self, driver):
        main_page = MainPage(driver)
        main_page.go_to_login_page_via_personal_account()

        login_page = LoginPage(driver)
        login_page.click_recover_password_field()

        recovery_page = RecoveryPage(driver)
        recovery_page.enter_email()
        recovery_page.click_recover_button()
        assert (
            recovery_page.is_reset_password_page()
        ), "Не выполнен переход на страницу установки нового пароля"

    @allure.title(
        "Клик по кнопке показать/скрыть пароль "
        "делает поле активным — подсвечивает его"
    )
    def test_password_toggle_makes_password_visible(self, driver):
        main_page = MainPage(driver)
        main_page.go_to_login_page_via_personal_account()
        login_page = LoginPage(driver)
        login_page.click_recover_password_field()

        recovery_page = RecoveryPage(driver)
        recovery_page.enter_email()
        recovery_page.click_recover_button()
        assert (
            recovery_page.is_reset_password_page()
        ), "Не выполнен переход на /reset-password"
        recovery_page.enter_password()
        recovery_page.toggle_password_visibility()
        assert (
            recovery_page.is_password_field_active()
        ), "Поле пароля не стало активным после клика по глазу"
