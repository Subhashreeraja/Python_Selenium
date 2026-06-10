import pytest
from selenium import webdriver
@pytest.fixture()
def setup_and_teardown(request):
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://demoblaze.com/")
    print("Demoblaze application launched successfully...")
    request.cls.driver = driver   
    yield
    driver.quit()