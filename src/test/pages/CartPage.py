from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class CartPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def go_to_cart(self):
        cart_icon = self.wait.until(EC.presence_of_element_located((AppiumBy.XPATH,
                                                                    '(//android.widget.ImageView[@resource-id="com.amazon.mShop.android.shopping:id/bottom_tab_button_icon"])[3]')))
        cart_icon.click()

    def delete_item(self):
        delete_button = self.wait.until(
            EC.presence_of_element_located((AppiumBy.XPATH, '//android.widget.Button[@text="Delete"]')))
        delete_button.click()

    def get_empty_cart_message(self):
        empty_cart_message = self.wait.until(EC.presence_of_element_located(
            (AppiumBy.XPATH, "//android.widget.TextView[@text=\"Your Amazon Cart is empty\"]")))
        return empty_cart_message.text

    def go_to_home(self):
        cart_icon = self.wait.until(EC.presence_of_element_located(
            (AppiumBy.XPATH, '//android.widget.ImageView[@content-desc="Home Tab 1 of 4"]')))
        cart_icon.click()

    def go_to_pick_up_left_off(self):
        left_off_option = self.wait.until(EC.presence_of_element_located(
            (AppiumBy.XPATH, "//android.widget.TextView[@text=\"Pick up where you left off\"]")))
        left_off_option.click()

    def selected_item_left_off(self):
        left_off_item = self.wait.until(EC.presence_of_element_located(
            (AppiumBy.XPATH,
             "//android.view.ViewGroup[@content-desc=\"Sheet\"]/android.widget.HorizontalScrollView/android.view.ViewGroup/android.view.ViewGroup")))
        left_off_item.click()

    def get_cart_count(self):
        cart_count = self.wait.until(
            EC.presence_of_element_located((AppiumBy.ID, "com.amazon.mShop.android.shopping:id/cart_count")))
        return cart_count.text
