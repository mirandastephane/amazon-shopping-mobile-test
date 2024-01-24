import unittest

from src.test.core.UtilMethods import UtilMethods
from src.test.managers.DriverManagerLocal import DriverManagerLocal
from src.test.pages.HelpPage import HelpPage
from src.test.pages.HomePage import HomePage
from src.test.pages.SideMenuPage import SideMenuPage


class CustomerServiceTest(unittest.TestCase):
    def setUp(self):
        self.driver_manager = DriverManagerLocal()
        self.driver = self.driver_manager.create_driver()

    def test_access_knowledge_base(self):
        home_page = HomePage(self.driver)
        side_menu_page = SideMenuPage(self.driver)
        util_methods = UtilMethods(self.driver)
        help_page = HelpPage(self.driver)

        home_page.go_to_menu()
        side_menu_page.select_item_menu("cs")
        help_page.select_item_option("Cancel Items or Orders")
        util_methods.perform_swipe_action(599, 2795)
        util_methods.perform_swipe_action(661, 403)
        help_page.click_button_yes()

        thank_you_message = help_page.get_thank_you_message()
        expected_text = "Thank you for your feedback."

        self.assertEqual(thank_you_message, expected_text, "Mensagem não encontrada!")
