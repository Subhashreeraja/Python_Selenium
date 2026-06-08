from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.maximize_window()
wait=WebDriverWait(driver,10)

driver.get("https://www.leafground.com/")

driver.find_element(By.XPATH,"//i[@class='pi pi-globe layout-menuitem-icon']").click()
driver.find_element(By.XPATH,"//span[text()='Alert']").click()

print("Clicked Alert")

driver.find_element(By.XPATH,"//div[@class='card']//child::button[@id='j_idt88:j_idt104']").click()

wait.until(EC.alert_is_present())

print("Clicked Prompt Alert")

alert=driver.switch_to.alert
alert.send_keys("OK")
alert.accept()

al2=driver.find_element(By.XPATH,"//span[@id='confirm_result']")

print(al2.text)

driver.quit()