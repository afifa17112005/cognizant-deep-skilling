from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get("https://www.lambdatest.com/selenium-playground/")

# Click "Simple Form Demo"
driver.find_element(By.LINK_TEXT, "Simple Form Demo").click()

assert "simple-form-demo" in driver.current_url
print("Current URL:", driver.current_url)

driver.back()
print("Returned to:", driver.title)

driver.quit()
