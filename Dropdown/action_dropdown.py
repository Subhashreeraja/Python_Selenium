
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import  WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.common.action_chains import ActionChains

driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.leafground.com/select.xhtml")

wait=WebDriverWait(driver,20)

drop_btn=wait.until(EC.element_to_be_clickable((By.XPATH, '//button[@type="button"]')))
drop_btn.click()

Playwright_option=wait.until(EC.visibility_of_element_located((By.XPATH,'//li[contains(.,"Playwright")]')))
action=ActionChains(driver)
action.move_to_element(Playwright_option).perform()
print("Playwright_option is selected using ActionChains")