from appium.webdriver.common.appiumby import AppiumBy

class HomePage:
    def __init__(self, driver):
        self.driver = driver

    def search_for_product(self, product_name):
        search_hint = self.driver.find_element(by=AppiumBy.ID, value="com.amazon.mShop.android.shopping:id/chrome_search_hint_view")
        search_hint.click()

        search_box = self.driver.find_element(by=AppiumBy.ID, value="com.amazon.mShop.android.shopping:id/rs_search_src_text")
        search_box.send_keys(product_name)