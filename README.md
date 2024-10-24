# Sauce Demo Automation

## Overview
This project automates the testing of the Sauce Demo e-commerce application ([https://www.saucedemo.com/](https://www.saucedemo.com/)) using Python, Selenium WebDriver, and pytest. It currenlty covers the following functionalities:
- **Login functionality**: Ensures users can log in with valid credentials and gets an error with invalid credentials.
- **Product listing**: Verifies that product details such as names, descriptions, and prices are displayed correctly.

The project is designed with scalability in mind, so additional functionality (such as cart operations, checkout, and other UI elements) can be easily incorporated in the future.
***Note**: The instructions in this document were verified on windows 11.*
## Project Structure

```plaintext
sauce_demo_automation/
│
├── README.md                    # Project overview and setup instructions
├── EXERCISE-1.md                # Specific exercise details and requirements
├── TEST-STRATEGY.md             # Test strategy document
├── TEST-PLANS.md                # Detailed test plans for features under test
├── DECISIONS_AND_REASONS.md     # Rationale for tool/framework choices
├── BUGREPORT-1.md               # Bug report template
│
├── tests/                       # Directory for test cases
│   ├── __init__.py
│   ├── test_login.py            # Test cases for login functionality
│   ├── test_product_listing.py  # Test cases for product listing
│   ├── test_cart.py             # Test cases for cart functionality
│   └── test_checkout.py         # Test cases for checkout process
│
├── pages/                       # Page Object Models
│   ├── __init__.py
│   ├── login_page.py            # Page methods for login page
│   ├── product_page.py          # Page methods for product listing and details
│   ├── cart_page.py             # Page methods for cart operations
│   └── checkout_page.py         # Page methods for checkout operations
│
├── utils/                       # Utility functions and helpers
│   ├── __init__.py
│   └── driver.py                # WebDriver setup and teardown
│
└── requirements.txt             # Python package dependencies
```

## Prerequisites
Before setting up and running the project, ensure that you have the following tools installed:

- Python 3.x
- pip (Python package installer)
- Google Chrome (the browser used for automating)
- Visual Studio Code (or any other IDE, optional)

## Installation 
### Clone the Repository 
- ``git clone https://github.com/yourusername/sauce_demo_automation.git``
- ``cd sauce_demo_automation``

### Create and Activate Virtual Environment
- ``python -m venv venv``

Activating it On Windows:

- ``venv\Scripts\activate``

### Install Dependencies
Install all required Python packages listed in requirements.txt:

- ``pip install -r requirements.txt``

## To run tests
To run all tests
- ``pytest``

***Note**: Running all tests is not recommended at this stage as some components are still under development and may not function as expected.*

To run a specific test file:e.g.
- ``pytest tests/test_login.py``

To run a specific test function: e.g. test_login_invalid_credentials functiona of login tests)
- ``pytest tests/test_login.py::test_login_invalid_credentials``

To run the test with verbose output add `--verbose`: e.g.
- ``pytest --verbose  test_product_listing.py``

To run the test with detailed output with full tracebacks add `--tb=long`: e.g.
- ``pytest --tb=long``

To run the test with print output for debugging add `-s`: e.g.
- `` pytest -s test_login.py``



## Test Strategy
The test strategy is documented in TEST-STRATEGY.md. It explains the testing approach, priorities, and scope of coverage for this project.

## Test Plans
The test plans are outlined in TEST-PLANS.md, describing specific test cases for each feature under test.

## Decisions and Rationale
The reasoning behind the choice of tools, frameworks, and testing strategies is explained in DECISIONS_AND_REASONS.md.

## Bug Reporting
A list of known issues and suggested improvements can be found in BUGREPORT-1.md. This document will be updated as new issues are discovered. The template used for reporting bugs includes the following fields:
### Bug: 
- **Ticket ID**: Unique identifier for tracking the issue.
- **Ticket Type**: Select from Bug/Improvement/Backlog (if not reproducible).
- **Severity**: Rate the impact on the application 
- **Priority**: High/Medium/Low, based on urgency.
- **Steps to Reproduce**:Detailed steps to reproduce the issue.
- **Expected Result**: What should happen under normal conditions.
- **Actual Result**: What actually happens when the issue occurs.
- **Screenshot**:  (Optional) Attach screenshots or evidence, if applicable.
- **Comments**: Additional information, context, or suggestions for resolving the issue.

## Test Coverage
Currently, the test suite covers:

**Login functionality**: Validates correct login and error handling for incorrect credentials.
**Product listing**: Verifies the correct display of product names, descriptions, and prices.










