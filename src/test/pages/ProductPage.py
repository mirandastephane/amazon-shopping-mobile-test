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
        add_to_cart_button = self.wait.until(EC.presence_of_element_located((AppiumBy.XPATH, '//android.widget.Button[@text="Add to cart"]')))
        add_to_cart_button.click()

    def add_to_cart_item_left_off(self):
        add_to_cart_item_left_off_button = self.wait.until(EC.presence_of_element_located((AppiumBy.XPATH, "(//android.widget.Button[@text=\"Add to Cart\"])[1]")))
        add_to_cart_item_left_off_button.click()

    def message_item_add(self):
        add_success = (AppiumBy.XPATH, "//android.widget.TextView[@text=\"Item Added\"]")
        message_add = self.wait.until(EC.presence_of_element_located(add_success))
        return message_add.text
