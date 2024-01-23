from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ProductPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def select_product(self, product_name):
        product_locator = (AppiumBy.XPATH, f'//android.widget.Button[@text="{product_name}"]')
        product_button = self.wait.until(EC.presence_of_element_located(product_locator))
        product_button.click()

    def add_to_cart(self):
        add_to_cart_button = self.wait.until(EC.presence_of_element_located((AppiumBy.XPATH, '//android.widget.Button[@resource-id="add-to-cart-button"]')))
        add_to_cart_button.click()