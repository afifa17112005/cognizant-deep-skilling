from pages.simple_form_page import SimpleFormPage
from pages.checkbox_page import CheckboxPage
from pages.dropdown_page import DropdownPage
from pages.input_form_page import InputFormPage

BASE='https://www.lambdatest.com/selenium-playground/'

def test_simple_form_submission(driver):
    page=SimpleFormPage(driver)
    page.navigate_to(BASE+'simple-form-demo')
    page.enter_message('Hello Selenium')
    page.click_submit()
    assert page.get_displayed_message()=='Hello Selenium'

def test_checkbox_demo(driver):
    page=CheckboxPage(driver)
    page.navigate_to(BASE+'checkbox-demo')
    page.check_option(0)
    assert page.is_option_checked(0)

def test_dropdown_selection(driver):
    page=DropdownPage(driver)
    page.navigate_to(BASE+'select-dropdown-demo')
    page.select_day('Wednesday')

def test_input_form_submit(driver):
    page=InputFormPage(driver)
    page.navigate_to(BASE+'input-form-demo')
    page.fill_form('John','john@test.com','9876543210','Chennai')
    page.submit_form()
