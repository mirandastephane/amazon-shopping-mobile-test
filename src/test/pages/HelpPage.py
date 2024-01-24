from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class HelpPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def select_item_option(self, option_name):
        option_locator = (AppiumBy.XPATH, f"//android.view.View[@content-desc=\"{option_name}\"]/android.view.View")
        option_button = self.wait.until(EC.presence_of_element_located(option_locator))
        option_button.click()

    def click_button_yes(self):
        yes_button = self.wait.until(
            EC.presence_of_element_located((AppiumBy.XPATH, '//android.widget.Button[@text=\"Yes\"]')))
        yes_button.click()

    def get_thank_you_message(self):
        thank_you_message = self.wait.until(EC.presence_of_element_located(
            (AppiumBy.XPATH, '//android.widget.TextView[@text=\"Thank you for your feedback.\"]')))
        return thank_you_message.text
