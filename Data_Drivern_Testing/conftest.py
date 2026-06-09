import pytest
from selenium import webdriver
import read_config
@pytest.fixture()
def test_setup_and_teardown(request):
    driver=webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(10)
    driver.get("https://www.demoblaze.com/index.html")
    request.cls.driver=driver
    yield
    driver.quit()