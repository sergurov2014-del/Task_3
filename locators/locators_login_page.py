# Локаторы страницы https://qa-stellarburgers.education-services.ru/login
from selenium.webdriver.common.by import By

EMAIL_INPUT = (By.XPATH, "//input[@type='text']")
PASSWORD_INPUT = (By.XPATH, "//input[@type='password']")
ENTER_BUTTON = (By.XPATH, "//button[text()='Войти']")
REGISTER_LINK = (By.XPATH, "//a[text()='Зарегистрироваться']")
RECOVERY_LINK = (By.XPATH, "//a[text()='Восстановить пароль']")
PASSWORD_EYE_TOGGLE = (By.XPATH, "//div[contains(@class,'input__icon-action')]")
