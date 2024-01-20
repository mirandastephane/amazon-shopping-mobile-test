import unittest

from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver import ActionChains
from selenium.webdriver.common.actions import interaction
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput

from src.test.core.UtilMethods import UtilMethods
from src.test.managers.DriverManagerLocal import DriverManagerLocal


class ShoppingCartTest(unittest.TestCase):
    def setUp(self):
        self.driver_manager = DriverManagerLocal()
        self.driver = self.driver_manager.create_driver()



    def test_add_to_cart(self):

        expect_text = "Your Amazon Cart is empty"

        el1 = self.driver.find_element(by=AppiumBy.ID, value="com.amazon.mShop.android.shopping:id/chrome_search_hint_view")

        el1.click()

        el2 = self.driver.find_element(by=AppiumBy.ID, value="com.amazon.mShop.android.shopping:id/rs_search_src_text")

        el2.send_keys("airdots")

        el2 = self.driver.implicitly_wait(5)

        el3 = self.driver.find_element(by=AppiumBy.XPATH, value="(//android.widget.Button[@text=\"airdots 3\"])[1]")

        el3.click()

        el3 = self.driver.implicitly_wait(5)

        el4 = self.driver.find_element(by=AppiumBy.XPATH,
                                  value="//android.view.View[@resource-id=\"search\"]/android.view.View[2]/android.view.View")
        el4.click()

        el4 = self.driver.implicitly_wait(5)

        el5 = self.driver.find_element(by=AppiumBy.XPATH,value="//android.widget.Image[@resource-id=\"main-image\"]")

        el5 = self.driver.implicitly_wait(5)

        actions = ActionChains(self.driver)
        actions.w3c_actions = ActionBuilder(self.driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
        actions.w3c_actions.pointer_action.move_to_location(546, 1564)
        actions.w3c_actions.pointer_action.pointer_down()
        actions.w3c_actions.pointer_action.move_to_location(553, 464)
        actions.w3c_actions.pointer_action.release()
        actions.perform()

        el6 = self.driver.find_element(by=AppiumBy.XPATH,
                                value="//android.widget.Button[@resource-id=\"add-to-cart-button\"]")

        el6.click()

        el6 = self.driver.implicitly_wait(5)

        el7 = self.driver.find_element(by=AppiumBy.XPATH,
                                       value="(//android.widget.ImageView[@resource-id=\"com.amazon.mShop.android.shopping:id/bottom_tab_button_icon\"])[3]")

        el7.click()

        el8 = self.driver.find_element(by=AppiumBy.XPATH, value="//android.widget.Button[@text=\"Delete\"]")

        el8.click()

        el9 = self.driver.find_element(by=AppiumBy.XPATH,
                                value="(//android.widget.ImageView[@resource-id=\"com.amazon.mShop.android.shopping:id/bottom_tab_button_icon\"])[3]")

        el9.click()

        el10 = self.driver.find_element(by=AppiumBy.XPATH, value="//android.widget.TextView[@text=\"Your Amazon Cart is empty\"]").text

        assert el10 == expect_text, "Carrinho não está vazio"

