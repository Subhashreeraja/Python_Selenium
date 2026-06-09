import pytest
from selenium import webdriver

@pytest.fixture(params=["chrome", "firefox", "edge"])
def setup_and_teardown(request):

    if request.param == "chrome":
        driver = webdriver.Chrome()
        
    driver.maximize_window()
    driver.implicitly_wait(5)

    driver.get("https://tutorialsninja.com/demo/")

    request.cls.driver = driver
    yield

    driver.quit()