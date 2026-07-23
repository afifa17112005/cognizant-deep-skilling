from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_simple_form_submission(driver):
    driver.get("https://www.lambdatest.com/selenium-playground")
    driver.find_element(By.LINK_TEXT,"Simple Form Demo").click()
    msg="Hello Selenium"
    box=WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.ID,"user-message")))
    box.send_keys(msg)
    driver.save_screenshot("screenshots/step42_before_submit.png")
    driver.find_element(By.ID,"showInput").click()
    out=WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.ID,"message")))
    driver.save_screenshot("screenshots/step42_after_submit.png")
    assert out.text==msg

def test_checkbox_demo(driver):
    driver.get("https://www.lambdatest.com/selenium-playground")
    driver.find_element(By.LINK_TEXT,"Checkbox Demo").click()
    cb=WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.ID,"isAgeSelected")))
    driver.save_screenshot("screenshots/step43_before_click.png")
    cb.click()
    driver.save_screenshot("screenshots/step43_selected.png")
    assert cb.is_selected()
    cb.click()
    driver.save_screenshot("screenshots/step43_deselected.png")
    assert cb.is_selected() is False
