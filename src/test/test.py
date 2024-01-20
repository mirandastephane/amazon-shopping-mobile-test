# This sample code supports Appium Python client >=2.3.0
# pip install Appium-Python-Client
# Then you can paste this into a file and simply run with Python

from appium import webdriver
from appium.options.common.base import AppiumOptions
from appium.webdriver.common.appiumby import AppiumBy

# For W3C actions
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions import interaction
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput

options = AppiumOptions()
options.load_capabilities({
	"platformName": "Android",
	"appium:automationName": "UiAutomator2",
	"appium:appPackage": "com.amazon.mShop.android.shopping",
	"appium:appActivity": "com.amazon.mShop.home.HomeActivity",
	"appium:connectHardwareKeyboard": True,
	"appium:noReset": True,
	"appium:fullReset": False,
	"appium:ensureWebviewsHavePages": True,
	"appium:nativeWebScreenshot": True,
	"appium:newCommandTimeout": 3600
})

driver = webdriver.Remote("http://127.0.0.1:4723", options=options)

el1 = driver.find_element(by=AppiumBy.ID, value="com.amazon.mShop.android.shopping:id/chrome_search_hint_view")
el1.click()
el2 = driver.find_element(by=AppiumBy.XPATH, value="//android.widget.Button[@text=\"airdots 3\"]")
el2.click()
el3 = driver.find_element(by=AppiumBy.XPATH, value="//android.view.View[@resource-id=\"search\"]/android.view.View[2]/android.view.View")
el3.click()
actions = ActionChains(driver)
actions.w3c_actions = ActionBuilder(driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
actions.w3c_actions.pointer_action.move_to_location(776, 1088)
actions.w3c_actions.pointer_action.pointer_down()
actions.w3c_actions.pointer_action.move_to_location(769, 442)
actions.w3c_actions.pointer_action.release()
actions.perform()

actions = ActionChains(driver)
actions.w3c_actions = ActionBuilder(driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
actions.w3c_actions.pointer_action.move_to_location(657, 1482)
actions.w3c_actions.pointer_action.pointer_down()
actions.w3c_actions.pointer_action.move_to_location(676, 475)
actions.w3c_actions.pointer_action.release()
actions.perform()

actions = ActionChains(driver)
actions.w3c_actions = ActionBuilder(driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
actions.w3c_actions.pointer_action.move_to_location(531, 1088)
actions.w3c_actions.pointer_action.pointer_down()
actions.w3c_actions.pointer_action.pause(0.1)
actions.w3c_actions.pointer_action.release()
actions.perform()

el4 = driver.find_element(by=AppiumBy.XPATH, value="(//android.widget.ImageView[@resource-id=\"com.amazon.mShop.android.shopping:id/bottom_tab_button_icon\"])[3]")
el4.click()

driver.quit()