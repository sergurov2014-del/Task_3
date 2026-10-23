# локаторы страницы восстановления пароля https://qa-stellarburgers.education-services.ru/forgot-password
from selenium.webdriver.common.by import By

EMAIL_INPUT = (By.XPATH, "//input[@type='text']")
PASSWORD_INPUT = (By.XPATH, "//input[@type='password']")
CODE_INPUT = (By.XPATH, "//input[@name='name']")
RECOVER_BUTTON = (By.XPATH, "//button[text()='Восстановить']")
SAVE_BUTTON = (By.XPATH, "//button[text()='Сохранить']")
ENTER_LINK = (By.XPATH, "//a[text()='Войти']")

PASSWORD_EYE_TOGGLE = (By.XPATH, "//div[contains(@class,'input__icon-action')]")
PASSWORD_CONTAINER=(By.XPATH, "//div[contains(@class, 'input_type_password')]")
PASSWORD_CONTAINER_ACTIVATED=(By.XPATH, "//div[contains(@class, 'input_status_active')]")