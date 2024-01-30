import unittest

from src.test.core.UtilMethods import UtilMethods
from src.test.managers.DriverManagerLocal import DriverManagerLocal
from src.test.pages.CancelItensPage import CancelItensPage
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
        cancel_itens_page = CancelItensPage(self.driver)

        option_text = "Cancel Items or Orders"

        home_page.go_to_menu()
        side_menu_page.select_item_menu("cs")
        help_page.validate_title_page("Customer Service")
        util_methods.perform_swipe_action(self.driver)
        # help_page.select_item_option(option_text)
        help_page.select_item_option("Cancel Items or Orders")
        cancel_itens_page.getTitlePage()


        expected_title = "Cancel Items and Orders"
        self.assertEqual(cancel_itens_page.getTitlePage(), expected_title, "Mensagem não encontrada!")
