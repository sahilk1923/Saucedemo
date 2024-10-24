# Title: Saucedemo Test Protocol 

## Introduction
The tests in this protocol achieve two things:
- They test the non-core software-related requirements in the Saucedemo Functional Requirement specification (let’s say DS 0003).
- They test the requirements in the Saucedemo Software Requirement specification (let’s say DS 0005).

## Scope
This document is part of the software verification described in the Saucedemo design and development plan (Let’s say DS 0001). This protocol is complemented by performance testing, security testing, and code reviews done for specific software requirements. The related requirements from DS 0003 and DS 0005 that are tested by each test step will be indicated beside that step.

## Assumptions

- There is a Saucedemo existing functional requirement (Version 1.0) and a Saucedemo software requirement (1.0)
- This protocol is specifically for **functional testing** and does **not** cover performance testing, usability studies, or security testing.
- Only alphabets and underscore are allowed as part of the username and password based on the username and password listed on the login page.

## Document References

| Document No | Document Title                                         | Version |
|-------------|-------------------------------------------------------|---------|
| e.g. DS 0001     | Saucedemo Design and Development Plan    | 1.0     |
| e.g. DS 0003     | Saucedemo Functional Requirement Spec.    | 1.0     |
| e.g. DS 0005     | Saucedemo Software Requirement Spec.      | 1.0     |
| e.g. TS 0001     | Test Strategy for Sauce Demo E-Commerce Application    | 1.0     |

## Acronyms

| Acronym | Definition           |
|---------|----------------------|
| e.g. OS      | Operating System      |
| e.g. FS      | Functional Specification|
| e.g. SRS     | Software Requirement Specification|
## Training Method
**Level 1, 2, or 3**

| Full Name       | Signature | Initials | Date       |
|-----------------|-----------|----------|------------|
| e.g. Sahil Kumar | SK        | SK       | 15/10/2024 |

## Build Configuration
Web application version number: 



## Equipment Details

| ID | Laptop Serial |
|----|---------------|
| e.g. 1  |      FA0267         |



## Test Environment
- **Application URL**: [Sauce Demo Application](https://www.saucedemo.com/)

| ID | Browser                    | Operating System                          | Device                   |
|----|---------------------------|------------------------------------------|--------------------------|
| e.g. 1  | Chrome 129.0.6668.90      | Windows 11 Version 0.0.22631 Build 22631 | Dell Laptop Inspiron 5491 |


## Protocol Execution and reporting
After ensuring that the preconditions are met, perform each test according to the steps detailed in the test table. Mark each test as pass or fail according to the acceptance criteria. Any incident associated with the execution of this protocl shall be documented in incident report and DroneShield issue tracking system(as requirerd).

This Test plan is structured so that the tester can print out this document and enter the test results onto the print-out, with the overall results summarized in Section – Completion. 




## Test Cases for E-commerce Web Application
**Notes**: 
- Add test for products availability, quantity and all
- test for browser compatibiluity and device compatibilty and different resolution can be done.
- Zoom/Resize behavior: Check how the screen behaves when zooming in or resizing the window.
-  Result and comment field can be added for every test cases
- **Menu Button**
   - Verifying the hamburger menu options: All Items, About, Logout, Reset App State, and close button.


### Test Case: Home Page Loading
- **Test Title**: Home Page Loading Verification
- **Test ID**: e.g. TC001
- **Precondition**: User is not logged in.
- **Test Steps**:
  1. Open the web application.
  2. Verify that the home page is loaded.
  3. Check for the presence of main elements: title, Username and password input field, login button.
- **Expected Result**: Home page must load without errors, and all key elements must be visible.

---

### Test Case: Login Functionality
- **Test Title**: Login with Valid Credentials
- **Test ID**: e.g. TC002
- **Precondition**: User has valid credentials.
- **Test Steps**:
  1. Navigate to the login page.
  2. Enter valid username and password.
  3. Click on the 'Login' button.
- **Expected Result**:  The user must be successfully logged in and redirected to the product listing page or inventory page.

---

### Test Case: Login Error Message for Invalid Credentials
- **Test Title**: Login with Invalid Credentials
- **Test ID**: 
- **Precondition**:N/A
- **Test Steps**:
    1. Navigate to the login page.
    2. Enter the username "locked_out_user" and password "secret_sauce".
    3. Click on the 'Login' button.
- **Expected Result**:  Error message must be displayed, informing the user that the login credentials are incorrect.

---

### Test Case: Login as Locked Out User
- **Test Title**: Login with Locked Out User
- **Test ID**:
- **Precondition**: User attempts to log in using `locked_out_user`.
- **Test Steps**:
  1. Navigate to the login page.
  2. Enter `locked_out_user` as the username and a valid password.
  3. Click the 'Login' button.
- **Expected Result**: An error message **shall** be displayed, informing the user that they are locked out and cannot access the application. The user **must** not be logged in.

---

### Test Case: Verify Product Image Display
- **Test Title**: Product Image Verification
- **Test ID**:
- **Precondition**: User is logged in and on the product listing page.
- **Test Steps**:
  1. Navigate to the product listing page.
  2. Verify that each product must display an image.
  3. Check that each image is the correct one for its respective product.
- **Expected Result**: All product images shall be correctly displayed, and each must correspond to its respective product.

---

### Test Case: Verify Product Name
- **Test Title**: Product Name Verification
- **Test ID**:
- **Precondition**: User is logged in and on the product listing page.
- **Test Steps**:
  1. Navigate to the product listing page.
  2. Verify that each product **must** display its name.
  3. Ensure the name **shall** be legible, correctly spelled, and associated with the correct product.
- **Expected Result**: All product names **must** be displayed correctly and **shall** match the corresponding product.

---

### Test Case: Verify Product Description
- **Test Title**: Product Description Verification
- **Test ID**:
- **Precondition**: User is logged in and on the product listing page.
- **Test Steps**:
  1. Navigate to the product listing page.
  2. Verify that each product must have a description displayed under its name.
  3. Ensure that the description shall accurately describe the product's features.
- **Expected Result**: Every product must have a description, and it shall be accurate and relevant to the product.

---

### Test Case: Usability Test for Product Image Size
- **Test Title**: Verify Product Image Size on Product Listing
- **Test ID**:
- **Precondition**: User is logged in, products are displayed on the product listing page.
- **Test Steps**:
  1. Navigate to the product listing page.
  2. Measure the size of the product image.
- **Expected Result**: Product image size must be at least 200x200(lets say) pixels to ensure clarity and usability.

---

### Test Case: Verify Loading Time of Product Page
- **Test Title**: Product Page Loading Time Verification
- **Test ID**:
- **Precondition**: User is logged in and accessing the product listing page.
- **Test Steps**:
  1. Navigate to the product listing page.
  2. Measure the time taken for the page to load completely, including product images, names, and descriptions.
- **Expected Result**: The product listing page should load within an acceptable time frame (e.g., 2 seconds). Images, names, and descriptions must be loaded without any delays or errors.

---

### Test Case: Verify Zoom/Resize Behavior on Product Page
- **Test Title**: Zoom/Resize Behavior Verification
- **Test ID**:
- **Precondition**: User is logged in and on the product listing or product details page.
- **Test Steps**:
  1. Navigate to the product page.
  2. Zoom in and out using browser controls.
  3. Resize the browser window to various sizes (e.g., maximize, minimize, mobile screen sizes).
  4. Check the layout and readability of product images, descriptions, and buttons.
- **Expected Result**: The screen shall adjust properly to zoom and resize actions. Text, images, and buttons must remain legible and accessible across all zoom levels and screen sizes.

---

### Test Case: Check Cart Button Visibility
- **Test Title**: Cart Button Display and Navigation
- **Test ID**:
- **Precondition**: User is logged in, and a product is added to the cart.
- **Test Steps**:
  1. Add a product to the cart.
  2. Verify the cart button is visible in the navigation bar.
  3. Click the cart button.
  4. Verify that it navigates to the cart summary page.
- **Expected Result**: The cart button must be visible, and clicking it should navigate to the cart summary.

---

### Test Case: Add to Cart Functionality
- **Test Title**: Add Product to Cart
- **Test ID**:
- **Precondition**: User is logged in, products are available on the inventory page.
- **Test Steps**:
  1. Select a product from the product list.
  2. Click the 'Add to Cart' button.
  3. Check the cart for the selected product.
  4. Verify that 
- **Expected Result**: The product must be added to the cart, and the cart should display the correct quantity and price.

---

### Test Case: Verify Checkout Process with Valid Details
- **Test Title**: Checkout Process Verification
- **Test ID**:
- **Precondition**: User has products added to the cart.
- **Test Steps**:
  1. Click on the 'Cart' button.
  2. Proceed to the checkout by clicking 'Checkout'.
  3. Enter valid user information (first name, last name, postal code).
  4. Complete the checkout process.
  5. Verify that an order confirmation message is displayed.
- **Expected Result**: The order must be successfully placed, and the user shall be presented with an order confirmation message.

---

### Test Case: Verify Checkout Process with Missing Details
- **Test Title**: Negative Test - Checkout Process with Missing Details
- **Test ID**:
- **Precondition**: User has products added to the cart.
- **Test Steps**:
  1. Click on the 'Cart' button.
  2. Proceed to the checkout by clicking 'Checkout'.
  3. Attempt to complete the checkout process without entering required details (e.g., leave postal code empty).
  4. Verify that an error message is displayed indicating that all required fields must be filled in.
- **Expected Result**: The system shall display an error message indicating that all required fields must be filled in, and the checkout process shall not be completed until valid information is provided.

---

### Test Case: Verify Checkout Process with Incorrect Details
- **Test Title**: Negative Test - Checkout Process with Incorrect Details
- **Test ID**: 
- **Precondition**: User has products added to the cart.
- **Test Steps**:
  1. Click on the 'Cart'  button.
  2. Proceed to the checkout by clicking 'Checkout'.
  3. Enter incorrect details (e.g., invalid postal code or name).
  4. Attempt to complete the checkout process.
  5. Verify that an error message is displayed indicating that all valid fields must be filled in.
- **Expected Result**: The system shall display an error message indicating the incorrect details, and the checkout process must not be completed until valid information is provided.

---

### Test Case: Verify Total Calculations in Checkout
- **Test Title**: Total Calculation Verification
- **Test ID**: 
- **Precondition**: User has multiple products added to the cart.
- **Test Steps**:
  1. Click on the 'Cart' button.
  2. Verify the subtotal matches the sum of the individual product prices.
  3. Apply any shipping charges or discounts.
  4. Verify the total amount displayed matches the expected total after considering all charges.
- **Expected Result**: The system must correctly calculate the subtotal, shipping charges, tax charges and total amount, ensuring the final total is accurate.

---

### Test Case: Verify Checkout Final Confirmation with Internet Disconnection
- **Test Title**: Negative Test - Checkout Process with Internet Disconnection
- **Test ID**: 
- **Precondition**: User is about to complete the checkout process.
- **Test Steps**:
  1. Add products to the cart and proceed to checkout.
  2. Before clicking on 'Confirm', disconnect the internet connection.
  3. Attempt to complete the checkout process.
  4. Verify that the system notifies the user of site not reachable.
- **Expected Result**: The system must notify the user of the site not reachable and shall prevent the checkout process from being completed. No order confirmation should be displayed, and the user must be prompted to reconnect and retry.

---

### Test Case: Verify Checkout Final Confirmation with Payment Rejection
- **Test Title**: Negative Test - Checkout Process with Payment Rejection
- **Test ID**: 
- **Precondition**: User has valid checkout details but enters incorrect payment details.
- **Test Steps**:
  1. Add products to the cart and proceed to checkout.
  2. Enter incorrect payment details (e.g., expired credit card or insufficient funds).
  3. Attempt to complete the checkout process.
  4. Verify that the system rejects the payment and displays an appropriate error message.
- **Expected Result**: The system shall reject the payment and display an appropriate error message, preventing the order confirmation from being displayed until valid payment details are provided.

---

### Test Case: Verify Checkout Final Confirmation with Insufficient Inventory
- **Test Title**: Negative Test - Checkout Process with Insufficient Inventory
- **Test ID**: 
- **Precondition**: User is attempting to purchase a product with limited stock.
- **Test Steps**:
  1. Add a product to the cart that has limited or no stock available.
  2. Proceed to checkout and attempt to complete the order.
  3. Verify that the system notifies the user if the product is out of stock or has insufficient inventory.
- **Expected Result**: The system shall notify the user if the product is out of stock or has insufficient inventory and prevent the checkout process from completing.

---

### Test Case: Error Handling for Empty Cart
- **Test Title**: Empty Cart Message
- **Test ID**:
- **Precondition**: User is logged in, and the cart is empty.
- **Test Steps**:
  1. Navigate to the cart page.
  2. Verify that an appropriate message is displayed when no products are in the cart.
- **Expected Result**: The message "Your cart is empty" should be displayed when no products are added to the cart.

---

### Test Case: Default Name A to Z Sorting
- **Test Title**: Verify Default Sorting from A to Z
- **Test ID**: 
- **Precondition**: User is logged in and on the product listing page.
- **Test Steps**:
  1. Navigate to the inventory or product listing page.
  2. Verify that the products are displayed in alphabetical order from A to Z by default.
  3. Verify that the default of the filter is 'Name (A to Z)'
- **Expected Result**: Products must be sorted alphabetically from A to Z by default.

---

### Test Case: Name Z to A Filter
- **Test Title**: Verify Name Z to A Sorting
- **Test ID**: 
- **Precondition**: User is logged in and on the product listing page.
- **Test Steps**:
  1. Navigate to the inventory or product listing page.
  2. Select the 'Name (Z to A)' filter.
  3. Verify the order of products displayed from Z to A by name.
- **Expected Result**: Products must be sorted alphabetically from Z to A.

---

### Test Case: Price Low to High Filter
- **Test Title**: Verify Price Low to High Sorting
- **Test ID**: 
- **Precondition**: User is logged in and on the product listing page.
- **Test Steps**:
  1. Navigate to the inventory or product listing page.
  2. Select the 'Price (Low to High)' filter.
  3. Verify the order of products displayed from lowest to highest price.
- **Expected Result**: Products must be sorted with the lowest price at the top and the highest at the bottom.

---

### Test Case: Price High to Low Filter
- **Test Title**: Verify Price High to Low Sorting
- **Test ID**: 
- **Precondition**: User is logged in and on the product listing page.
- **Test Steps**:
  1. Navigate to the inventory or product listing page.
  2. Select the 'Price (High to Low)' filter.
  3. Verify the order of products displayed from highest to lowest price.
- **Expected Result**: Products must be sorted with the highest price at the top and the lowest at the bottom.

---

#### Test Case: Menu Button - All Items

- **Test Title**: Verify All Items Menu Option
- **Test ID**: 
- **Precondition**: User is logged in and on the product listing page.
- **Test Steps**:
  1. Click on the menu button (three lines).
  2. Select the "All Items" option from the menu.
  3. Verify that the user is navigated to the product listing page (inventory page) displaying all available items.
- **Expected Result**: User must be navigated to the product listing page (inventory page) displaying all available items.

---

#### Test Case: Menu Button - About

- **Test Title**: Verify About Menu Option
- **Test ID**: 
- **Precondition**: User is logged in and on the product listing page.
- **Test Steps**:
  1. Click on the menu button (three lines).
  2. Select the "About" option from the menu.
  3. Verify that the user is taken to the About screen displaying application information.
- **Expected Result**: User must be taken to the About screen displaying application information.

---

#### Test Case: Menu Button - Logout
- **Test Title**: Verify Logout Menu Option
- **Test ID**: 
- **Precondition**: User is logged in.
- **Test Steps**:
  1. Click on the menu button (three lines).
  2. Select the "Logout" option from the menu.
  Verify that the user is logged out and redirected to the login page.
- **Expected Result**: User must be logged out and redirected to the login page.

---

#### Test Case: Menu Button - Reset App State
- **Test Title**: Verify Reset App State Menu Option
- **Test ID**: 
- **Precondition**: User has items in the cart.
- **Test Steps**:
  1. Click on the menu button (three lines).
  2. Select the "Reset App State" option from the menu.
  3. Verify that the cart is cleared and the user sees an empty cart.
- **Expected Result**: The cart must be cleared, and the user should see an empty cart.

---

#### Test Case: Menu Button - Close Button
- **Test Title**: Verify Close Button Functionality
- **Test ID**: 
- **Precondition**: User is logged in and the menu is open.
- **Test Steps**:
  1. Click on the menu button (three lines).
  2. Click on the "Close" button.
  3. Verify that the menu closes, returning the user to the product listing page.
- **Expected Result**: The menu must close, and the user must return to the product listing page.

---

#### Test Case: Going Back from About Screen
- **Test Title**: Verify Navigation Back from About Screen
- **Test ID**: 
- **Precondition**: User is on the About screen.
- **Test Steps**:
  1. Click the back button or any available navigation option to return to the previous page.
  2. Verify that the user is navigated back to the product listing page.
- **Expected Result**: User must be navigated back to the product listing page.

---

### Test Case: Freestyle Negative Test – Invalid Characters in Input Fields

- **Test Title**: Invalid Characters in Input Fields
- **Test ID**: 
- **Precondition**: User is on the login or checkout page.
- **Test Steps**:
  1. Enter a string with special characters (e.g., `#$%^&*()`) in the username field on the login page and enter a valid password in the password field.
  2. Click the 'Login' button.
  3. Verify that an error message is displayed for invalid characters in the username field.
  4. Enter a string with special characters (e.g., `#$%^&*()`) in the password field on the login page and enter a valid username in the username field.
  5. Click the 'Login' button.
  6. Verify that an error message is displayed for invalid characters in the username field.
  7. On the checkout page, enter a string with special characters in the following fields:
     - First Name
     - Last Name
     - Zip/Postal Code
  8. Click the 'Continue' button after entering invalid characters in the checkout fields.
  9. Verify that error messages are displayed for each field where invalid characters were entered, preventing submission of the form.
- **Expected Result**: 
  - An error message must be displayed for each field where invalid characters were entered, preventing submission of the form.
  - The system should not crash or behave unexpectedly during the test.

---

### Test Case: Session Timeout
- **Test Title**: Verify Session Timeout After Predefined Period
- **Test ID**: 
- **Precondition**: User is logged in and actively browsing the website.
- **Test Steps**:
  1. Log in to the application.
  2. Perform normal activities (e.g., add items to the cart, browse product pages).
  3. Leave the session idle for the predefined session timeout duration (e.g., 20 minutes).
  4. After the timeout duration, try to navigate to a new page or perform any action.
  5. Verify that the user is automatically logged out and redirected to the login page.
- **Expected Result**: The user must be automatically logged out after the session timeout period, and any subsequent action shall redirect them to the login page. The cart and session data should persist, and the user must be able to log back in to continue where they left off.

---

### Test Case: Inactivity Timeout
- **Test Title**: Verify Inactivity Timeout for Inactive Users
- **Test ID**: 
- **Precondition**: User is logged in and has initiated activity on the application (e.g., filling out a form or browsing a page).
- **Test Steps**:
  1. Log in to the application.
  2. Begin performing some actions (e.g., navigate to checkout or start filling a form).
  3. Leave the session idle for a certain inactivity timeout period (e.g., 15 minutes) without interacting with the page.
  4. Attempt to interact with the page after the inactivity timeout period expires.
  5. Verify that the session has expired and the user is prompted to log back in.
- **Expected Result**: After the predefined period of inactivity, the session shall expire, and the user must be automatically logged out. The system shall prompt the user to log back in, retaining session data where applicable (e.g., cart data).

---

### Test Case: Continuous Usage Timeout
- **Test Title**: Verify Continuous Usage Timeout After Extended Active Session
- **Test ID**: 
- **Precondition**: User is logged in and actively using the application for an extended period (e.g., continuously browsing, adding items to the cart, checking out).
- **Test Steps**:
  1. Log in to the application.
  2. Continuously use the application for an extended period (e.g., 4-8 hours) without any breaks.
  3. After the continuous usage timeout threshold (e.g., 6 hours), attempt to continue using the application.
  4. Verify that the application prompts the user to re-authenticate or restart the session.
- **Expected Result**: After the extended period of continuous use, the application should prompt the user to re-authenticate or restart the session for security reasons. The session must persist cart and user data after re-authentication.

---

### Test Case: Compare Page Content Against Reference Page

- **Test Title**: Verify that the current page content matches the reference page.
- **Test ID**: 
- **Precondition**: User is logged in and on the page to be tested. A reference page (or snapshot) is available for comparison.
- **Test Steps**:
  1. Navigate to the web page that needs to be compared.
  2. Load the reference page or snapshot for comparison.
  3. Check the following elements on the current page against the reference:
     - Page layout (header, footer, sidebars)
     - Product names, descriptions, and images
     - Text formatting, fonts, and colors
     - Button placement and functionality
     - Links and navigation
  4. Verify that each element matches the reference page in terms of layout, content, and style.
- **Expected Result**: The current page **must** match the reference page in terms of layout, text, product images, descriptions, and functionality. Any discrepancies **shall** be reported as defects.

---

### Test Case: Random Inventory Actions

- **Test Title**: Freestyle Testing of Inventory Page
- **Test ID**: 
- **Precondition**: User is logged in and on the inventory page with items available.
- **Test Steps**:
  1. Randomly select a product and add it to the cart.
  2. Remove the same product from the cart.
  3. Repeat adding and removing multiple products.
  4. Change the sorting options (e.g., Price Low to High, Name Z to A).
  5. Click on product images to ensure they open in a detailed view.
  6. Change the quantity of an item in the cart and verify the cart updates correctly.
  7. Check the 'Continue Shopping' button to ensure it navigates correctly.
  8. Refresh the inventory page and verify that the previous state (e.g., items in cart, selected filters) is maintained.
- **Expected Result**: 
  - All actions must perform correctly without errors.
  - The cart must reflect the correct items after adding/removing.
  - Navigation between pages and product views shall function as expected.
  - Refreshing the page should not disrupt the user experience or cause errors.

## Attachments

## Summary Report




|                  | Full Name      | Signature | Initials | Date       |
|------------------|----------------|-----------|----------|------------|
| Completed By     | e.g. Sahil Kumar | SK        | SK       | 15/10/2024 |
| Reviewed By      |                  |           |          |            |
| Reviewed By      |                  |           |          |            |





