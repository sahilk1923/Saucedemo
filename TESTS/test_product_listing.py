# tests/test_product_listing.py
# this test can be extended looking to verify the picture links, menu options, 
import pytest
# from pages.login_page import LoginPage
from pages.product_page import ProductPage
# from utils.driver import get_driver

class TestProductListing:
    # @pytest.fixture(scope="class", autouse=True)
    # def setup_class(self):
    # @pytest.fixture(autouse=True)  # Autouse applies this fixture to every test in the class
    # def setup(self):
    #     self.driver = get_driver()
    #     self.login_page = LoginPage(self.driver)
    #     self.product_page = ProductPage(self.driver)
    #     self.login_page.navigate_to_login()
    #     self.login_page.enter_username("standard_user")
    #     self.login_page.enter_password("secret_sauce")
    #     self.login_page.click_login()
    #     yield
    #     if self.driver:
    #         self.driver.quit()
    @pytest.fixture(autouse=True)
    def setup(self, login):  # Using 'login' fixture to ensure user is logged in
        self.product_page = ProductPage(login)

    def test_page_title(self):
        expected_title = "Swag Labs"  # Replace with the actual title of the page
        assert self.product_page.verify_page_title(expected_title), "Page title is incorrect."

    def test_page_logo(self):
        expected_logo = "Swag Labs"  # Replace with the actual title of the page
        assert self.product_page.verify_page_logo(expected_logo), "page Logo is incorrect."


    def test_product_count(self):
        expected_product_count = 6  # Update with the actual expected number of products
        assert len(self.product_page.get_inventory_items()) == expected_product_count, "Product count mismatch."

    def test_product_details(self):
        # Define expected product details
        # Product 6 description is intentionally incorrect
        expected_details = [
            {
                "name": "Sauce Labs Backpack",
                "description": "Carry all the things with the sleek, streamlined Sly Pack that melds uncompromising style with unequaled laptop and tablet protection.",
                "price": "$29.99"
            },
            {
                "name": "Sauce Labs Bike Light",
                "description": "A red light isn't the desired state in testing but it sure helps when riding your bike at night. Water-resistant with 3 lighting modes, 1 AAA battery included.",
                "price": "$9.99"
            },
            {
                "name": "Sauce Labs Bolt T-Shirt",
                "description": "Get your testing superhero on with the Sauce Labs bolt T-shirt. From American Apparel, 100% ringspun combed cotton, heather gray with red bolt.",
                "price": "$15.99"
            },
            {
                "name": "Sauce Labs Fleece Jacket",
                "description": "It's not every day that you come across a midweight quarter-zip fleece jacket capable of handling everything from a relaxing day outdoors to a busy day at the office.",
                "price": "$49.99"
            },
            {
                "name": "Sauce Labs Onesie",
                "description": "Rib snap infant onesie for the junior automation engineer in development. Reinforced 3-snap bottom closure, two-needle hemmed sleeved and bottom won't unravel.",
                "price": "$7.99"
            },
            {
                "name": "Sauce Labs T-Shirt (Red)",
                "description": "This classic Sauce Labs t-shirt is perfect to wear when cozying up to your keyboard to automate a few tests. Super-soft and comfy ringspun combed cotton.",
                "price": "$15.99"
            }
        ]

        # Verify product details
        success, message = self.product_page.verify_product_details(expected_details)
        assert success, message

    # def test_menu_button_displayed(product_page):
    #     assert product_page.is_menu_button_displayed(), "Menu button is not displayed."

    # def test_cart_button_displayed(product_page):
    #     assert product_page.is_cart_button_displayed(), "Cart button is not displayed."
        
    
    # def test_product_display(self):
    #     product_titles = self.product_page.get_product_titles()
    #     product_descriptions = self.product_page.get_product_descriptions()
    #     product_prices = self.product_page.get_product_prices()

    #     assert len(product_titles) > 0, "No products displayed."
    #     assert len(product_descriptions) == len(product_titles), "Mismatch in product descriptions."
    #     assert len(product_prices) == len(product_titles), "Mismatch in product prices."

    # # def test_add_to_cart(self):
    # #     initial_cart_count = len(self.driver.find_elements_by_class_name("shopping_cart_badge"))
    # #     self.product_page.add_product_to_cart()
    # #     updated_cart_count = len(self.driver.find_elements_by_class_name("shopping_cart_badge"))
    # #     assert updated_cart_count == initial_cart_count + 1, "Cart count did not increase after adding a product."

    # def test_sorting_price_low_to_high(self):
    #     self.product_page.select_sort_option("Price (low to high)")
    #     prices = self.product_page.get_product_prices()
    #     price_values = [float(price.replace("$", "")) for price in prices]
    #     assert price_values == sorted(price_values), "Products not sorted by price low to high."

    # def test_sorting_name_a_to_z(self):
    #     self.product_page.select_sort_option("Name (A to Z)")
    #     titles = self.product_page.get_product_titles()
    #     assert titles == sorted(titles), "Products not sorted by name A to Z."
