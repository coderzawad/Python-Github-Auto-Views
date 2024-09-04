from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

# Set up the WebDriver
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

# URL to visit
url = "https://github.com/coderzawad"

try:
    # Open 10 tabs
    for _ in range(10):
        driver.execute_script("window.open('');")

    # Get all the tabs
    tabs = driver.window_handles

    # Visit the URL in each tab initially
    for tab in tabs:
        driver.switch_to.window(tab)
        driver.get(url)
        print(f"Visited {url}")

    while True:
        # Reload all tabs simultaneously
        for tab in tabs:
            driver.switch_to.window(tab)
            driver.execute_script("setTimeout(() => { window.location.reload(); }, 0);")
            print(f"Triggered reload for {url} in tab {tab}")

        # Wait for 10 seconds before the next reload (optional)

except KeyboardInterrupt:
    # If interrupted, close the driver
    print("Stopping automation.")
    driver.quit()
