# # tests/test_cart.py
# # this is not tested
# import pytest
# from pages.login_page import LoginPage
# from pages.product_page import ProductPage
# from pages.cart_page import CartPage
# from utils.driver import get_driver

# class TestCart:
#     # @pytest.fixture(scope="class", autouse=True)
#     @pytest.mark.skip(reason="Work in progress")
#     def setup_class(self):
#         self.driver = get_driver()
#         self.login_page = LoginPage(self.driver)
#         self.product_page = ProductPage(self.driver)
#         self.cart_page = CartPage(self.driver)
#         self.login_page.navigate_to_login()
#         self.login_page.enter_username("standard_user")
#         self.login_page.enter_password("secret_sauce")
#         self.login_page.click_login()
#         # self.product_page.add_product_to_cart()
#         # self.product_page.navigate_to_cart()
#         yield
#         self.driver.quit()
#     @pytest.mark.skip(reason="Work in progress")
#     def test_cart_contains_added_product(self):
#         cart_items = self.cart_page.get_cart_items()
#         assert len(cart_items) > 0, "Cart is empty but should contain added products."
#     @pytest.mark.skip(reason="Work in progress")
#     def test_remove_product_from_cart(self):
#         initial_cart_count = len(self.cart_page.get_cart_items())
#         self.cart_page.remove_item_from_cart()
#         updated_cart_count = len(self.cart_page.get_cart_items())
#         assert updated_cart_count == initial_cart_count - 1, "Cart count did not decrease after removing a product."
#     @pytest.mark.skip(reason="Work in progress")
#     def test_cart_empty_after_removal(self):
#         self.cart_page.remove_item_from_cart()
#         assert self.cart_page.is_cart_empty(), "Cart is not empty after removing all products."
