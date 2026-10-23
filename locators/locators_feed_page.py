# локаторы страницы
from selenium.webdriver.common.by import By

READY_ORDERS_LIST = (By.CSS_SELECTOR, "[class*='OrderFeed_orderList']")
IN_WORK_ORDERS_LIST = (By.XPATH, "//ul[contains(@class,'OrderFeed_orderListReady')]/li")
ORDER_FEED_LIST = (By.XPATH, "//ul[contains(@class,'OrderFeed_list')]")
ORDER_FEED_ITEMS_LINK = (By.CSS_SELECTOR, "[class*='OrderFeed_list'] > li a")
FEED_OVERLAY_MODAL_OPENED=(By.XPATH,"//section[contains(@class,'Modal_modal_opened')]")

TOTAL_COMPLETED_COUNTER = (
    By.XPATH,
    "//p[text()='Выполнено за все время:']/following-sibling::p",
)
TODAY_COMPLETED_COUNTER = (
    By.XPATH,
    "//p[text()='Выполнено за сегодня:']/following-sibling::p",
)


ORDER_FEED_ITEMS = (By.XPATH, "//ul[contains(@class,'OrderFeed_list')]/li")
ORDER_NUMBER_IN_FEED = (By.XPATH, ".//p[contains(@class,'text_type_digits-default')]")