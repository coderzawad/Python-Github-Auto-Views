from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

# Set up the WebDriver
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

# URL to visit
url = "https://github.com/samiulalimseam"

try:
    while True:
        # Open the URL
        driver.get(url)
        print(f"Visited {url}")
        
        # Wait for 10 seconds before the next visit
        time.sleep(10)

except KeyboardInterrupt:
    # If interrupted, close the driver
    print("Stopping automation.")
    driver.quit()
