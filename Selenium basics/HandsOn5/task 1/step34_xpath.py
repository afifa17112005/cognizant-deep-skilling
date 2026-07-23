from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import os

os.makedirs("screenshots", exist_ok=True)

driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://www.lambdatest.com/selenium-playground/")

driver.find_element(By.LINK_TEXT,"Checkbox Demo").click()

label=driver.find_element(By.XPATH,"//label[text()='Option 1']")
labels=driver.find_elements(By.XPATH,"//label[contains(text(),'Option')]")

print("First:",label.text)
print("Count:",len(labels))
driver.save_screenshot("screenshots/step34.png")
driver.quit()
