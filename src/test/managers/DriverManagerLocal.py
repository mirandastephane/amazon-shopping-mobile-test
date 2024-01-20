from appium.options.common import AppiumOptions
from selenium import webdriver


class DriverManagerLocal:

    def __init__(self):
        # self.option = option
        # self.driver = driver
        pass
    def create_driver(self):
        appium_options = AppiumOptions()
        appium_options.load_capabilities({
            "platformName": "Android",
            "appium:automationName": "UiAutomator2",
            "appium:appPackage": "com.amazon.mShop.android.shopping",
            "appium:appActivity": "com.amazon.mShop.home.HomeActivity",
            "appium:connectHardwareKeyboard": True,
            "appium:noReset": True,
            "appium:fullReset": False,
        })

        remote_url = "http://localhost:4723"

        driver = webdriver.Remote(remote_url, options=appium_options)
        return driver


