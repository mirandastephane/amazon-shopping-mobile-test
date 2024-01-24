from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class SideMenuPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def select_item_menu(self, option_name):
        item_locator = (AppiumBy.XPATH, f"//android.view.View[@resource-id=\"{option_name}\"]")
        item_button = self.wait.until(EC.presence_of_element_located(item_locator))
        item_button.click()
