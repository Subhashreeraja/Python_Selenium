import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

driver=webdriver.Chrome()

driver.maximize_window()
driver.get("https://www.leafground.com/select.xhtml")
time.sleep(3)

select_element=driver.find_element(By.XPATH,'//select[@class="ui-selectonemenu"]')
Select=Select(select_element)
time.sleep(3)


Select.select_by_visible_text("Selenium")
Select.select_by_index(3)

time.sleep(3)

print("Selenium is selected")
print("3 rd index is selected")
print(Select.first_selected_option.text)
time.sleep(3)

# Select.deselect_by_value(3) facing an error like NotImplementedError: You may only deselect options of a multi-select


