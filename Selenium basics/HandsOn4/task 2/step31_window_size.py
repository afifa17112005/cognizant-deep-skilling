from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get("https://www.lambdatest.com/selenium-playground/")

print("Current Window Size:", driver.get_window_size())

# Consistent window size ensures UI elements render consistently
# across different executions and screen resolutions.
driver.set_window_size(1280, 800)

print("Updated Window Size:", driver.get_window_size())

driver.quit()
