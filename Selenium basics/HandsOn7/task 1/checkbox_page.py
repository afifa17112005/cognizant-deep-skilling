from selenium.webdriver.common.by import By
from .base_page import BasePage

class CheckboxPage(BasePage):
    CHECKBOXES=(By.CSS_SELECTOR,"input[type='checkbox']")

    def check_option(self,index):
        cb=self.driver.find_elements(*self.CHECKBOXES)[index]
        if not cb.is_selected():
            cb.click()

    def uncheck_option(self,index):
        cb=self.driver.find_elements(*self.CHECKBOXES)[index]
        if cb.is_selected():
            cb.click()

    def is_option_checked(self,index):
        return self.driver.find_elements(*self.CHECKBOXES)[index].is_selected()
