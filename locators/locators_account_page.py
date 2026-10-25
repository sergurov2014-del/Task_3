# Локаторы страницы профиля https://qa-stellarburgers.education-services.ru/account/profile
from selenium.webdriver.common.by import By

ACCOUNT_TITLE = (By.XPATH, "//p[text()= 'Личный Кабинет']")
PROFILE_BUTTON = (By.XPATH, "//a[text()='Профиль']")
ORDER_HISTORY_BUTTON = (By.XPATH, "//a[text()='История заказов']")
EXIT_BUTTON = (By.XPATH, "//button[text()='Выход']")


ORDER_HISTORY_ITEMS = (By.XPATH, "//ul[contains(@class,'OrderHistory_list')]/li")
ORDER_NUMBER_IN_HISTORY = (By.XPATH, ".//p[contains(@class,'text_type_digits-default')]")
ORDER_HISTORY_CREATED_ORDER_NUMBERS_LIST=(By.XPATH,"//li[contains(@class, 'OrderHistory_list')]/a/div/p[contains(@class, 'text_type_digits-default')]")
