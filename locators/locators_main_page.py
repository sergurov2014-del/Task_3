# локаторы главной страницы
from selenium.webdriver.common.by import By

CONSTRUCTOR_BUTTON = (By.XPATH, '//p[contains(text(),"Конструктор")]')
ORDER_FEED_BUTTON = (By.XPATH, "//p[contains(text(), 'Лента Заказов')]")
PERSONAL_ACCOUNT_LINK = (By.XPATH, '//p[text()="Личный Кабинет"]')

LOGIN_BUTTON = (By.XPATH, "//button[contains(text(), 'Войти в аккаунт')]")
CREATE_ORDER_BUTTON = (By.XPATH, '//button[text()="Оформить заказ"]')


MODAL_OVERLAY = (By.CSS_SELECTOR, "[class*='Modal_modal_overlay']")

ALL_INGEDIENT_CARDS = (By.XPATH, "//a[contains(@class,'BurgerIngredient_ingredient')]")
CARDS_COUNTER = (By.XPATH, ".//p[contains(@class,'counter_counter__num')]")

CONSTRUCTOR_BASKET = (
    By.XPATH,
    "//section[contains(@class,'BurgerConstructor_basket')]",
)
INGREDIENT_INFORMATION_MODAL_WINDOW = (By.XPATH, "//h2[text()='Детали ингредиента']")

CLOSE_MODAL_WINDOW_BUTTON = (
    By.XPATH,
    "//h2[text()='Детали ингредиента']/parent::div//following-sibling::button[contains(@class,'Modal_modal__close')]",
)

ORDER_IDENTIFICATOR_FIELD = (By.XPATH, "//p[text()='идентификатор заказа']")
ORDER_IS_COOKING_FIELD = (By.XPATH, "//p[text()='Ваш заказ начали готовить']")
FIELD_WITH_NUMBER_OF_ORDER_IDENTIFICATOR = (By.XPATH,"//h2[contains(@class, 'Modal_modal__title_shadow')]")
