## Задание 3: 

# Diplom_3: UI-тесты для Stellar Burgers
3 часть дипломного проекта с UI-автотестами для приложения Stellar Burgers - https://qa-stellarburgers.education-services.ru

## Стек

| Инструмент | Назначение |
|------------|-----------|
| Python ≥ 3.10 | Язык написания тестов |
| Selenium 4 | WebDriver для управления браузером |
| pytest | Тестовый фреймворк |
| Allure | Генерация HTML-отчётов |
| Faker | Генерация тестовых данных |
| requests | API-вызовы (регистрация, логин, удаление пользователя) |

## Паттерны и подходы

- **Page Object Model** — каждой странице соответствует класс в `pages/` и файл локаторов в `locators/`
- **Фикстуры pytest** — логин и создание заказа вынесены в `conftest.py`; регистрация через API
- **API-регистрация** — пользователи создаются через `POST /api/auth/register`, а не через UI
- **Allure** — тесты и методы покрыты `@allure.step()`, `@allure.feature`, `@allure.story`
- **Faker** — тестовые данные генерируются динамически, без хардкода
- **Два браузера** — Chrome и Firefox запускаются через `pytest.mark.parametrize`


## Структура проекта

```
.
├── locators/              # Локаторы (Selenium By-tuples)
│   ├──__init__.py         # Cпециальный файл, который превращает обычную папку в Python-пакет
│   ├──locators_account_page.py
│   ├── locators_feed_page.py
│   ├── locators_login_page.py
│   ├── locators_main_page.py
│   ├── locators_recovery_pass_page.py 
│   └── locators_register_page.py
│
├── pages/                 # Page Object классы
│   ├──__init__.py - специальный файл, который превращает обычную папку в Python-пакет
│   ├── base_page.py       # Базовый класс: click/js_click, find_element/s, send_keys, get_text, wait, open, contains
│   ├── main_page.py       # Конструктор бургеров, навигация, drag-and-drop
│   ├── login_page.py      # Страница входа
│   ├── account_page.py    # Личный кабинет
│   ├── feed_page.py       # Лента заказов
│   └── recovery_password_page.py   # Восстановление пароля
│   
│
├── tests/                         # Тесты
│   ├──__init__.py                 # Cпециальный файл, который превращает обычную папку в Python-пакет
│   ├── conftest.py                # Фикстуры: driver,authorized_user_driver
│   ├── test_feed_orders.py        # 5 тестов: лента заказов
│   ├── test_main_functional.py    # 6 тестов: основной функционал   
│   ├── test_personal_account.py   # 3 теста: личный кабинет
│   └── test_recover_password.py   # 3 теста: восстановление пароля
│
├── requirements.txt       # Зависимости
├── __init__.py           # специальный файл, который превращает обычную папку в Python-пакет
├── helpers.py             # вспомогательный функции 
├── .gitignore             # файлы не загружаемые в git
├── urls.py                # ссылки на 

```

## Установка и запуск

```bash
#Создание requirements.txt
pip install pipreqs
pipreqs . --force --encoding=utf-8

# Установка зависимостей
pip install -r requirements.txt

# Запуск всех тестов (Chrome + Firefox )
python -m  pytest ./tests 

# Запуск только Chrome
python -m pytest -k chrome

# Запуск только Firefox
python -m pytest -k firefox

# Запуск тестов конкретного файла
python -m pytest tests/test_main_functional.py

# Расширенный запуск одного теста по имени
python -m pytest tests/test_personal_account.py::TestPersonalAccount::test_go_to_personal_account_from_main -k chrome -v --tb=long

# Генерация Allure-отчёта
python -m  pytest ./tests --alluredir=allure_results
allure serve allure_results
```

## API-эндпоинты для тестов

Тестовые пользователи (email, password, name) создаются через `POST /api/auth/register` (`helpers.py`):


## Реализованные тест-кейсы: 17 тестов. Проверка производилась в 2 браузерах Google Chrome и FireFox. Суммарно 34 теста

### Восстановление пароля
- Переход на страницу восстановления по кнопке «Восстановить пароль»
- Ввод почты и клик по «Восстановить»
- Клик по кнопке показать/скрыть пароль делает поле активным - подсвечивает поле

### Личный кабинет
- Переход по клику на «Личный кабинет»
- Переход в раздел «История заказов»
- Выход из аккаунта

### Основной функционал
- Переход по клику на «Конструктор»
- Переход по клику на «Лента заказов»
- Клик по ингредиенту вызывает модальное окно с деталями
- Закрытие модального окна кликом по крестику
- Счётчик ингредиента увеличивается при добавлении ингредиента в заказ (через drag-and-drop)
- Залогиненный пользователь может оформить заказ

### Лента заказов
- Клик по заказу открывает модальное окно с деталями
- Заказы пользователя из раздела «История заказов» отображаются на странице «Лента заказов»,
- При создании нового заказа  счётчик «Выполнено за всё время» увеличивается
- При создании нового заказа счётчик «Выполнено за сегодня» увеличивается
- после оформления заказа его номер появляется в разделе  «В работе»
