from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Implicit wait applies to every element lookup.
# In real projects Explicit Waits are preferred because
# they wait only for specific elements and avoid unnecessary delays.
driver.implicitly_wait(10)

driver.get("https://www.lambdatest.com/selenium-playground/")
print("Page Title:", driver.title)

driver.quit()
