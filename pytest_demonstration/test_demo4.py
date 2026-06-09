import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions

@pytest.mark.parametrize('input_browser', ['chrome'])
@pytest.mark.parametrize('input_url',['https://www.flipkart.com/','https://www.amazon.in/'])
def test_google_search(input_browser, input_url):

    if input_browser == 'chrome':
        options = ChromeOptions()
        options.add_argument("--headless=new")
        driver = webdriver.Chrome(options=options)

    driver.maximize_window()
    driver.get(input_url)

    print(driver.title)

    driver.quit()