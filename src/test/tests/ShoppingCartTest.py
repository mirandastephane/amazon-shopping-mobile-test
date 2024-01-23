import unittest
from appium.webdriver.common.appiumby import AppiumBy
from src.test.pages.HomePage import HomePage
from src.test.pages.ProductPage import ProductPage
from src.test.pages.CartPage import CartPage
from src.test.managers.DriverManagerLocal import DriverManagerLocal


class ShoppingCartTest(unittest.TestCase):
    def setUp(self):
        self.driver_manager = DriverManagerLocal()
        self.driver = self.driver_manager.create_driver()

    def test_add_to_cart(self):
        home_page = HomePage(self.driver)
        product_page = ProductPage(self.driver)
        cart_page = CartPage(self.driver)

        home_page.search_for_product("airdots")
        product_page.select_product("airdots 3")
        product_page.add_to_cart()
        cart_page.go_to_cart()
        cart_page.delete_item()

        empty_cart_message = cart_page.get_empty_cart_message()
        expected_text = "Your Amazon Cart is empty"

        self.assertEqual(empty_cart_message, expected_text, "Carrinho não está vazio")


if __name__ == "__main__":
    unittest.main()