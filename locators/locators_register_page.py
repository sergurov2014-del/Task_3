# Локаторы страницы https://qa-stellarburgers.education-services.ru/register
from selenium.webdriver.common.by import By

NAME_INPUT = (By.XPATH, "//label[text()='Имя']/following-sibling::input")
EMAIL_INPUT = (By.XPATH, "//label[text()='Email']/following-sibling::input")
PASSWORD_INPUT = (By.XPATH, "//input[@type='password']")
REGISTRATE_BUTTON = (By.XPATH, "//button[text()='Зарегистрироваться']")
ENTER_BUTTON = (By.XPATH, "//a[text()='Войти']")
