from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class CancelItensPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def getTitlePage(self):
        textTitle = self.wait.until(EC.presence_of_element_located(
            (AppiumBy.XPATH,
             "//android.widget.TextView[@resource-id=\"GUID-8823A89C-2772-4CA6-9644-30621B4672FD__GUID-1522E8A9-5031-467D-A776-7B00C9E48E73\"]")))
        return textTitle.text
