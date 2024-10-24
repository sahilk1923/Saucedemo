# Test Strategy for Sauce Demo E-Commerce Application

## Introduction
The purpose of this Test Strategy document is to outline the testing approach for the Sauce Demo e-commerce application. This document will cover the objectives, scope, and methodology to ensure the application meets quality standards through a combination of manual and automated testing. 

## Objectives
- To validate the functionality of key features of the application, including login, product listing,filtering and sorting products,cart, and checkout processes.
- To ensure the application is free from critical defects before release.
- To evaluate some techinical aspects of usability uch as layout and navigation, while noting that true usability requires actual user testing.
## Scope
The following features will be included in the testing scope:
- **Login Page**: Testing the functionality of username, password, login button, and valid username/password combinations.
- **Product Listing Page**: Verifying product details (name, description, image, price), add to cart functionality, and sorting/filtering options.
- **Menu Button**: Testing menu options including "All Items," "About," "Logout," "Reset App State," and the close button.
- **Cart Functionality**: Ensuring items are correctly added/removed from the cart and reflected on the cart page.
- **Checkout Process**: Testing the checkout flow, including data input (first name, last name, postal code), order review, and completion.

## Assumptions
- The application will be available in a stable state during the testing period.
- All required resources (test data, hardware, software) will be accessible.
- Testers will have the necessary permissions to access the application.
- The login username and password will only support alphabets (A-Z, a-z) and underscores (_).
- This protocol is focused on **functional testing**, and **performance testing**, **security testing**  will not be included.

## Testing Types
1. **Functional Testing**: Verify that the application functions as expected.
2. **Usability Testing**: Assess the user experience and interface design.

## Testing Environment
The testing will be performed on the Sauce Demo application hosted at `https://www.saucedemo.com/`.
- **Devices**: 
  - Laptop: Various Windows and MacBook models.
  - Mobile: iPhone (latest iOS), Android devices (Samsung Galaxy, Google Pixel).
  - Tablets: iPad (latest iOS), Android tablets (Samsung Galaxy Tab).
- **Browsers**: Chrome, Firefox, Edge.
- **Operating Systems**: Windows 10, Windows 11, Linux (Ubuntu or other common distributions).


## Testing Tools
- **Automation Framework**: Selenium with Python for automated testing.
- **Bug Tracking Tool**: Jira for logging and tracking defects.


## Conclusion
This Test Strategy provides a comprehensive overview of the testing approach for the Sauce Demo e-commerce application. The objective is to ensure the application meets quality standards and delivers a positive user experience.
