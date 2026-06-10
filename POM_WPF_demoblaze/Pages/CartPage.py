from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
class CartPage:
    
    def __init__(self,driver):
        self.driver=driver
        
    def verify_product_added_in_the_cart(self):
        wait=WebDriverWait(self.driver,20)
        cart_link_text=wait.until(EC.element_to_be_clickable((By.XPATH,'//a[text()="Cart"]')))
        cart_link_text.click()
        product_title=wait.until(EC.element_to_be_clickable((By.XPATH,'//tr[@class="success"]//descendant::td[text()="MacBook Pro"]')))
        return product_title.text
        
           