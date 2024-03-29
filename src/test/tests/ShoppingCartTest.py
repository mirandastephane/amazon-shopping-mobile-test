import unittest

from src.test.managers.DriverManagerLocal import DriverManagerLocal
from src.test.pages.CartPage import CartPage
from src.test.pages.HomePage import HomePage
from src.test.pages.ProductPage import ProductPage


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

        expected_add_message = "Item Added"
        self.assertEqual(product_page.message_item_add(), expected_add_message, "Mensagem não exibida")

        cart_page.go_to_cart()
        cart_page.delete_item()
        cart_page.go_to_cart()

        empty_cart_message = cart_page.get_empty_cart_message()
        expected_text = "Your Amazon Cart is empty"

        self.assertEqual(empty_cart_message, expected_text, "Carrinho não está vazio")

    def test_add_to_cart_left_off_item(self):
        product_page = ProductPage(self.driver)
        cart_page = CartPage(self.driver)

        cart_page.go_to_cart()
        cart_page.go_to_pick_up_left_off()
        cart_page.selected_item_left_off()

        product_page.add_to_cart_item_left_off()

        cart_page.go_to_cart()

        self.assertEqual(cart_page.get_cart_count(),"1","Carrinho não possui item adicionado!")

if __name__ == "__main__":
    unittest.main()
