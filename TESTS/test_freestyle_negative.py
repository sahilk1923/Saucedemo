# # tests/test_freestyle_negative.py
# # this is not tested
# import pytest
# from pages.login_page import LoginPage
# from pages.product_page import ProductPage
# from pages.cart_page import CartPage
# from pages.checkout_page import CheckoutPage
# from utils.driver import get_driver
# import time

# class TestFreestyleNegative:
#     @pytest.fixture(scope="class", autouse=True)
#     def setup_class(self):
#         self.driver = get_driver()
#         self.login_page = LoginPage(self.driver)
#         self.product_page = ProductPage(self.driver)
#         self.cart_page = CartPage(self.driver)
#         self.checkout_page = CheckoutPage(self.driver)
#         self.login_page.navigate_to_login()
#         yield
#         self.driver.quit()

#     def test_invalid_characters_in_login_and_checkout(self):
#         # Test invalid characters in login
#         self.login_page.enter_username("user!@#")
#         self.login_page.enter_password("pass%^&*")
#         self.login_page.click_login()
#         assert self.login_page.is_error_message_displayed(), "Error message not displayed for invalid login characters."

#         # Reset to login
#         self.login_page.navigate_to_login()
#         self.login_page.enter_username("standard_user")
#         self.login_page.enter_password("secret_sauce")
#         self.login_page.click_login()
#         assert self.login_page.is_login_successful(), "Login failed with valid credentials."

#         # Add to cart and proceed to checkout
#         self.product_page.add_product_to_cart()
#         self.product_page.navigate_to_cart()
#         self.cart_page.click_checkout()

#         # Enter invalid characters in checkout
#         self.checkout_page.enter_first_name("John$%^")
#         self.checkout_page.enter_last_name("Doe@#!")
#         self.checkout_page.enter_postal_code("12#45")
#         self.checkout_page.click_continue()
#         assert self.checkout_page.is_error_message_displayed(), "Error message not displayed for invalid checkout characters."

#     def test_random_inventory_actions(self):
#         # Add multiple products
#         for i in range(3):
#             self.product_page.add_product_to_cart()
#             time.sleep(1)  # Wait for UI updates

#         self.product_page.navigate_to_cart()
#         cart_items = self.cart_page.get_cart_items()
#         assert len(cart_items) == 3, "Incorrect number of items in the cart."

#         # Remove a product
#         self.cart_page.remove_item_from_cart()
#         cart_items = self.cart_page.get_cart_items()
#         assert len(cart_items) == 2, "Failed to remove item from cart."

#         # Add and remove randomly
#         self.product_page.navigate_to_cart()
#         self.cart_page.remove_item_from_cart()
#         self.cart_page.remove_item_from_cart()
#         assert self.cart_page.is_cart_empty(), "Cart is not empty after removing all items."

#         # Navigate back to products
#         self.driver.back()
#         assert "inventory.html" in self.driver.current_url, "Did not navigate back to product listing page."
