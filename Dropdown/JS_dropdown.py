
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import  WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.leafground.com/select.xhtml")

wait=WebDriverWait(driver,20)

drop_btn=wait.until(EC.element_to_be_clickable((By.XPATH, '//button[@type="button"]')))
drop_btn.click()

# select_div=driver.find_element(By.XPATH,'ui-autocomplete-items ui-autocomplete-list ui-widget-content ui-widget ui-corner-all ui-helper-reset')
react_js_option = wait.until( EC.presence_of_element_located((By.XPATH, '//li[contains(.,"ReactJs")]') ))
driver.execute_script('arguments[0].click()',react_js_option)

print("ReactJs is selected using js Executor")



