from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CartPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def go_to_cart(self):
        cart_icon = self.wait.until(EC.presence_of_element_located((AppiumBy.XPATH, '(//android.widget.ImageView[@resource-id="com.amazon.mShop.android.shopping:id/bottom_tab_button_icon"])[3]')))
        cart_icon.click()

    def delete_item(self):
        delete_button = self.wait.until(EC.presence_of_element_located((AppiumBy.XPATH, '//android.widget.Button[@text="Delete"]')))
        delete_button.click()

    def get_empty_cart_message(self):
        empty_cart_message = self.wait.until(EC.presence_of_element_located((AppiumBy.XPATH, '//android.widget.TextView[@text="Your Amazon Cart is empty"]')))
        return empty_cart_message.text