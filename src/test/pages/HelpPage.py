from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class HelpPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def select_item_option(self, option_name):
        # Esse locator não funcionou aqui, mas deixei comentado já que
        # option_locator = (AppiumBy.XPATH, f"//android.view.View[@content-desc=\"{option_name}\"]/android.view.View")

        option_locator = (AppiumBy.XPATH, "//android.widget.Button[@text=\"Cancel Items or Orders You can cancel items or orders that haven't entered the shipping process yet. Cancel Items or Orders\"]")
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

    def validate_title_page(self, title_text):
        self.wait.until(
            EC.presence_of_element_located((AppiumBy.XPATH, f"//android.widget.TextView[@text=\"{title_text}\"]")))

    def swipe(self):
        self.driver.execute_script("mobile: scroll", {"direction": "up"})
