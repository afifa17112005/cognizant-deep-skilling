from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os,time
os.makedirs("screenshots",exist_ok=True)
driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()))

from selenium.common.exceptions import NoSuchElementException

driver.get("https://www.lambdatest.com/selenium-playground/table-sort-search-demo")

wait=WebDriverWait(driver,10,poll_frequency=0.5,
                   ignored_exceptions=[NoSuchElementException])

table=wait.until(
 EC.visibility_of_element_located((By.ID,"example")))

print("Dynamic table loaded.")
driver.save_screenshot("screenshots/step39_fluent_wait.png")
driver.quit()
