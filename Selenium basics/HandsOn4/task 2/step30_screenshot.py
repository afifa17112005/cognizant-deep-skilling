from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import os

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get("https://www.lambdatest.com/selenium-playground/")

driver.execute_script("window.open('https://www.google.com');")
driver.switch_to.window(driver.window_handles[0])

filename = "playground_screenshot.png"
driver.save_screenshot(filename)

print("Screenshot Saved:", os.path.exists(filename))

driver.quit()
