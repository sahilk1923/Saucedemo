# Sauce Demo E-Commerce Application

For this small size web application manual testing will be applicable but automation will be more useful if this app is going to change and we are add lot of other functionality

must shall, should 

assuming that this test protocol for comprehensive testing before release

test cases - 
SRS and FS can be added 
**Priority**: Medium
- **Type**: Functional, Usability


Documentation components can be changed based on the compliance and regulatory requirements

Automating the critical component of the web application
taking screenshots of the web pages and comparing against the golden references

test cases can be divided as per critical functioanality or just funcitonality wise

- This is a business-to-Consumer application.














# Decisions and Reasons

## 1. Framework Selection

### **Selenium WebDriver**
- **Reason**: Selenium is a powerful and widely-adopted tool for automating web applications. It supports multiple browsers and platforms, allowing comprehensive testing across different environments.
- **Benefit**: Flexibility in handling dynamic web elements and extensive community support.

### **pytest**
- **Reason**: pytest offers a simple syntax, powerful features like fixtures and parameterization, and excellent plugin support.
- **Benefit**: Facilitates writing scalable and maintainable test cases, and integrates seamlessly with reporting tools like pytest-html.

## 2. Design Pattern

### **Page Object Model (POM)**
- **Reason**: POM enhances test maintenance and reduces code duplication by encapsulating page-specific elements and actions within separate classes.
- **Benefit**: Improves readability and scalability of the test suite, making it easier to update tests when the UI changes.

## 3. Test Case Organization

### **Modular Structure**
- **Reason**: Organizing tests, page objects, and utilities into separate directories promotes clarity and scalability.
- **Benefit**: Facilitates easy navigation and management of the codebase, especially as the project grows.

## 4. WebDriver Management

### **Manual Setup of WebDriver**
- **Reason**: Provides control over the WebDriver version, ensuring compatibility with the browser version.
- **Benefit**: Avoids issues related to version mismatches and enhances reliability of the test execution environment.

## 5. Virtual Environment

### **Using `venv`**
- **Reason**: Isolates project dependencies from the system Python installation.
- **Benefit**: Prevents version conflicts and ensures consistent environments across different development setups.

### **6. TEST-STRATEGY.md**

Provide a high-level overview of testing approach.

### **7. TEST-PLANS.md**

Provide detailed test plans for each feature.

## Conclusion

The decisions made in selecting tools and designing the test automation project are aimed at ensuring a robust, maintainable, and scalable testing framework. By leveraging Selenium with Python and pytest, adhering to the Page Object Model, and maintaining a clean project structure, the automation suite is well-equipped to handle the testing requirements of the Sauce Demo e-commerce application effectively.
