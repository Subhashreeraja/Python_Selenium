
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import  WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.leafground.com/select.xhtml")

wait=WebDriverWait(driver,20)

drop_btn=wait.until(EC.element_to_be_clickable((By.XPATH, '//button[@type="button"]')))
drop_btn.click()


choose_bar=driver.find_element(By.XPATH,'//select[@class="ui-selectonemenu"]')
choose_bar.send_keys("JMeter")
choose_bar.send_keys(Keys.ENTER)
print("JMeter is selected using sendKeys")
