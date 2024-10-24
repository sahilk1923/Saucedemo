# pages/product_page.py
from selenium.webdriver.common.by import By

class ProductPage:
    def __init__(self, driver):
        self.driver = driver
       
        # self.page_title= (By.CLASS_NAME, "title")
        # # self.page_logo = (By.CLASS_NAME, "app_logo")
        # self.product_list=(By.CLASS_NAME, "inventory_list")

        # self.product_titles = (By.CLASS_NAME, "inventory_item_name")
        # self.product_descriptions = (By.CLASS_NAME, "inventory_item_desc")
        # self.product_prices = (By.CLASS_NAME, "inventory_item_price")
        # # self.add_to_cart_buttons = (By.CLASS_NAME, "btn_inventory")
        # self.cart_button = (By.CLASS_NAME, "shopping_cart_link")
        # self.sort_dropdown = (By.CLASS_NAME, "product_sort_container")

    # def verify_page_title(self,expected_title):
    #     return self.driver.find_elements(By.CLASS_NAME, 'inventory_item')

    def verify_page_title(self, expected_title):
        actual_title = self.driver.title  # Get the current page title
        
        print(f"here you go {actual_title}")
        return actual_title == expected_title  # Return True if the titles match
    
    def verify_page_logo(self, expected_logo):
        actual_logo = self.driver.find_element(By.CSS_SELECTOR, 'div.app_logo')  # Get the current page title
        actual_logo = actual_logo.text.strip()
        print(f"here you go {actual_logo}")
        return actual_logo == expected_logo  # Return True if the titles match

    def get_inventory_items(self):
        # Find all the inventory items on the page
        return self.driver.find_elements(By.CLASS_NAME, 'inventory_item')

    def get_product_name(self, product):
        # Within the given product (inventory_item), find the product name
        return product.find_element(By.CLASS_NAME, 'inventory_item_name').text

    def get_product_description(self, product):
        # Within the given product, find the product description
        return product.find_element(By.CLASS_NAME, 'inventory_item_desc').text

    def get_product_price(self, product):
        # Within the given product, find the price
        return product.find_element(By.CLASS_NAME, 'inventory_item_price').text

    def verify_product_details(self, expected_details):
        """
        Verify product details including name, description, and price.
        expected_details is a list of dictionaries, each containing expected name, description, and price.
        """
        products = self.get_inventory_items()

        errors = []  # Store all errors

        # Check if the number of products matches the expected number
        if len(products) != len(expected_details):
            # return False, f"Expected {len(expected_details)} products, but found {len(products)}."
            errors.append(f"Expected {len(expected_details)} products, but found {len(products)}.")

        # Loop through products and verify each product's details
        for index, product in enumerate(products):
            actual_name = self.get_product_name(product)
            actual_desc = self.get_product_description(product)
            actual_price = self.get_product_price(product)

            expected_name = expected_details[index]["name"]
            expected_desc = expected_details[index]["description"]
            expected_price = expected_details[index]["price"]

            if actual_name != expected_name:
                # return False, f"Expected name '{expected_name}', but got '{actual_name}'"
                errors.append(f"Product {index+1}: Expected name '{expected_name}', but got '{actual_name}'")
            if actual_desc != expected_desc:
                # return False, f"Expected description '{expected_desc}', but got '{actual_desc}'"
                errors.append(f"Product {index+1}: Expected description '{expected_desc}', but got '{actual_desc}'")
            if actual_price != expected_price:
                # return False, f"Expected price '{expected_price}', but got '{actual_price}'"
                errors.append(f"Product {index+1}: Expected price '{expected_price}', but got '{actual_price}'")
        
        if errors:
            return False, "\n".join(errors)  # Return all errors as a single string
        return True, "All product details match."

    # def add_product_to_cart(self, product_index=0):
    #     add_button = self.driver.find_elements(*self.add_to_cart_buttons)[product_index]
    #     add_button.click()

    # def navigate_to_cart(self):
    #     self.driver.find_element(*self.cart_button).click()

    # def select_sort_option(self, option_text):
    #     sort_element = self.driver.find_element(*self.sort_dropdown)
    #     sort_element.click()
    #     sort_element.find_element(By.XPATH, f"//option[text()='{option_text}']").click()
