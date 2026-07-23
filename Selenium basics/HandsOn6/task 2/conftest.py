import os
import pytest
from selenium import webdriver

os.makedirs("screenshots", exist_ok=True)

@pytest.fixture(scope="session")
def base_url():
    return "https://www.lambdatest.com/selenium-playground/"

@pytest.fixture(scope="function")
def driver(request):
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(10)
    request.node.driver = driver
    yield driver
    driver.quit()

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    if report.when == "call" and report.failed:
        drv = getattr(item, "driver", None)
        if drv:
            drv.save_screenshot(f"screenshots/{item.name}_failure.png")
