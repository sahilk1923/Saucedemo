# utils/driver.py
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
import os
import sys

def get_driver():
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")
    # Add more options if needed

    # Path to the ChromeDriver executable
    service = ChromeService(executable_path=os.getenv('CHROME_DRIVER_PATH', 'chromedriver'))
    
    # # Validate if the chromedriver path is valid
    # if not os.path.isfile(chromedriver_path):
    #     print(f"ChromeDriver not found at {'CHROME_DRIVER_PATH'}. Ensure CHROME_DRIVER_PATH is set correctly.", file=sys.stderr)
    #     sys.exit(1)

    # driver = webdriver.Chrome(service=service, options=chrome_options)


     # Using webdriver-manager to handle ChromeDriver automatically
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chrome_options)
    
    return driver


# # Explicitly set the chromedriver path
#     chromedriver_path = r'path/to/chromedriver'  # Replace with the correct path
#     service = ChromeService(executable_path=chromedriver_path)
#     chrome_options = webdriver.ChromeOptions()
    
#     driver = webdriver.Chrome(service=service, options=chrome_options)
#     return driver