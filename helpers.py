from faker import Faker
import requests
import urls
from pages.main_page import MainPage

fake = Faker()


def get_random_name():
    name = fake.name()
    return name


def get_random_email():
    email = fake.email()
    return email


def get_random_password():
    password = fake.password()
    return password


def register_user() -> (
    tuple[str, str, str]
):  # регистрирует пользователя через API. Возвращает пароль,
    email = get_random_email()
    password = get_random_password()
    name = get_random_name()
    payload = {
        "email": email,
        "password": password,
        "name": name,
    }  # {"email": email, "password": password, "name": name}
    response = requests.post(urls.API_REGISTER_URL, json=payload)

    # если понадобится удалить нужен будет токен data = response.json() accessToken = data["accessToken"]
    return email, password, name


def make_new_order(
    authorized_user_driver, index_1=1, index_2=3
):  # создаёт заказ авторизированным пользователем
    main_page = MainPage(authorized_user_driver)
    main_page.open()
    main_page.drag_and_drop_ingredient_to_constructor(index_1)
    main_page.drag_and_drop_ingredient_to_constructor(index_2)
    main_page.click_button_make_order()
    order_number = main_page.return_cooking_order_number()
    
    return order_number
