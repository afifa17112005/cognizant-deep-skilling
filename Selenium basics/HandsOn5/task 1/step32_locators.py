from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import os

os.makedirs("screenshots", exist_ok=True)

driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://www.lambdatest.com/selenium-playground/")

driver.find_element(By.LINK_TEXT,"Simple Form Demo").click()

locators=[
("ID",driver.find_element(By.ID,"user-message")),
("NAME",driver.find_element(By.NAME,"user-message")),
("CLASS_NAME",driver.find_element(By.CLASS_NAME,"form-control")),
("TAG_NAME",driver.find_element(By.TAG_NAME,"input")),
("ABS_XPATH",driver.find_element(By.XPATH,"/html/body/div[2]//input")),
("REL_XPATH",driver.find_element(By.XPATH,"//input[@id='user-message']"))
]

for n,e in locators:
    print(n,"OK:",e.get_attribute("id"))

driver.save_screenshot("screenshots/step32.png")
driver.quit()
