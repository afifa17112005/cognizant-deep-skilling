from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import os

os.makedirs("screenshots", exist_ok=True)

driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://www.lambdatest.com/selenium-playground/")

driver.find_element(By.LINK_TEXT,"Simple Form Demo").click()

css1=driver.find_element(By.CSS_SELECTOR,"#user-message")
css2=driver.find_element(By.CSS_SELECTOR,"input[name='user-message']")
css3=driver.find_element(By.CSS_SELECTOR,"div.col-md-6 input")

print(css1.get_attribute("id"),css2.get_attribute("id"),css3.get_attribute("id"))
driver.save_screenshot("screenshots/step33.png")
driver.quit()
