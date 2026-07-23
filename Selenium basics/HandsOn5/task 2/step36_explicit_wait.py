from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os,time
os.makedirs("screenshots",exist_ok=True)
driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get("https://www.lambdatest.com/selenium-playground/bootstrap-alert-messages-demo")
btn=WebDriverWait(driver,10).until(
 EC.element_to_be_clickable((By.XPATH,"//button[contains(.,'Success Message')]")))
btn.click()
alert=WebDriverWait(driver,10).until(
 EC.visibility_of_element_located((By.CSS_SELECTOR,".alert-success")))
print(alert.text)
assert "success" in alert.text.lower()
driver.save_screenshot("screenshots/step36_success_alert.png")
driver.quit()
