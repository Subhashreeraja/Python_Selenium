import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
@pytest.mark.parametrize('input_browser',[('chrome'),('firefox')])

@pytest.mark.parametrize('input_url',[('https://www.flipkart.com/'),('https://www.amazon.in/')])
def test_google_search(input_browser,input_url):
    
    if input_browser == 'chrome':
        options = ChromeOptions()
        options.add_argument("--headless")   
        driver = webdriver.Chrome(options=options)
      
    if input_browser == 'firefox':
        options = FirefoxOptions()
        options.add_argument("--headless")   
        driver = webdriver.Firefox(options=options) 
    driver.maximize_window()
    driver.get(input_url)
    print(driver.title)
    driver.close()