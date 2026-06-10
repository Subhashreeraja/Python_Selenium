from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ProductPage:
    def __init__(self,driver):
        self.driver=driver
        
    def click_add_to_cart_btn(self):
        wait=WebDriverWait(self.driver,20)
        cart_btn = wait.until(
        EC.visibility_of_element_located((By.XPATH, '//a[text()="Add to cart"]')))
        cart_btn.click()

        wait.until(EC.alert_is_present())
        alert=self.driver.switch_to.alert
        alert_text=alert.text
        alert.accept()
        return alert_text