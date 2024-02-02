from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class HomePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def search_for_product(self, product_name):
        search_hint = self.driver.find_element(by=AppiumBy.ID,
                                               value="com.amazon.mShop.android.shopping:id/chrome_search_hint_view")
        search_hint.click()

        search_box = self.driver.find_element(by=AppiumBy.ID,
                                              value="com.amazon.mShop.android.shopping:id/rs_search_src_text")
        search_box.send_keys(product_name)

    def go_to_menu(self):
        menu_icon = self.wait.until(EC.presence_of_element_located((AppiumBy.XPATH,
                                                                    '//android.widget.ImageView[@content-desc="Browse menu Tab 4 of 4"]')))
        menu_icon.click()
