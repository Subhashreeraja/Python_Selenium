import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
@pytest.mark.parametrize('search_term',[('selenium'),('pytest'),('web element locators')])

def test_google_search(search_term):
    
    driver=webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://www.google.com/")
    search_bar=driver.find_element(By.NAME,"q")
    search_bar.send_keys(search_term)
    search_bar.send_keys(Keys.ENTER)
    driver.quit()

