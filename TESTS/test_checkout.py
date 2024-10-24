# # tests/test_checkout.py
# # this is not tested
# import pytest
# from pages.login_page import LoginPage
# from pages.product_page import ProductPage
# from pages.cart_page import CartPage
# from pages.checkout_page import CheckoutPage
# from utils.driver import get_driver

# class TestCheckout:
#     @pytest.fixture(scope="class", autouse=True)
#     def setup_class(self):
#         self.driver = get_driver()
#         self.login_page = LoginPage(self.driver)
#         self.product_page = ProductPage(self.driver)
#         self.cart_page = CartPage(self.driver)
#         self.checkout_page = CheckoutPage(self.driver)
#         self.login_page.navigate_to_login()
#         self.login_page.enter_username("standard_user")
#         self.login_page.enter_password("secret_sauce")
#         self.login_page.click_login()
#         self.product_page.add_product_to_cart()
#         self.product_page.navigate_to_cart()
#         yield
#         self.driver.quit()

#     def test_checkout_with_valid_details(self):
#         self.cart_page.click_checkout()
#         self.checkout_page.enter_first_name("John")
#         self.checkout_page.enter_last_name("Doe")
#         self.checkout_page.enter_postal_code("12345")
#         self.checkout_page.click_continue()
#         # Assuming there's a summary page to verify
#         # You can add assertions here for summary
#         self.checkout_page.click_finish()
#         assert self.checkout_page.is_order_confirmation_displayed(), "Order confirmation not displayed."

#     def test_checkout_with_missing_details(self):
#         self.cart_page.click_checkout()
#         self.checkout_page.enter_first_name("")  # Missing first name
#         self.checkout_page.enter_last_name("Doe")
#         self.checkout_page.enter_postal_code("12345")
#         self.checkout_page.click_continue()
#         assert self.checkout_page.is_error_message_displayed(), "Error message not displayed for missing details."

#     def test_checkout_with_incorrect_details(self):
#         self.cart_page.click_checkout()
#         self.checkout_page.enter_first_name("John")
#         self.checkout_page.enter_last_name("Doe")
#         self.checkout_page.enter_postal_code("ABCDE")  # Invalid postal code
#         self.checkout_page.click_continue()
#         assert self.checkout_page.is_error_message_displayed(), "Error message not displayed for incorrect details."

#     def test_checkout_with_payment_rejection(self):
#         # This test assumes that entering invalid payment details triggers a payment rejection.
#         # Since Sauce Demo is a demo site, it might have specific behaviors for testing purposes.
#         self.cart_page.click_checkout()
#         self.checkout_page.enter_first_name("John")
#         self.checkout_page.enter_last_name("Doe")
#         self.checkout_page.enter_postal_code("12345")
#         self.checkout_page.click_continue()
#         self.checkout_page.click_finish()
#         assert self.checkout_page.is_order_confirmation_displayed(), "Order confirmation not displayed after payment rejection."
#         # Adjust based on actual behavior
