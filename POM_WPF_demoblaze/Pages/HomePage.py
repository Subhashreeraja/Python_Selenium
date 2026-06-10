from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
class HomePage:
         
     
    def __init__(self,driver):
        self.driver=driver
     
    def login(self,username,password):
        wait = WebDriverWait(self.driver,20)   
        wait.until(EC.element_to_be_clickable((By.ID, "login2"))).click()
        wait.until(EC.visibility_of_element_located((By.ID, "loginusername"))).send_keys(username)
        wait.until(EC.visibility_of_element_located((By.ID, "loginpassword"))).send_keys(password)
        wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Log in']"))).click()
        
    def verify_welcome_msg(self):
        wait = WebDriverWait(self.driver,20)
        
        # logout = self.driver.find_element(By.ID,"logout2")
        welcome_txt=wait.until(EC.visibility_of_element_located((By.ID, "nameofuser")))
        return welcome_txt.text
  
    def choose_categories_product(self):
        wait = WebDriverWait(self.driver,20)
        wait.until(EC.visibility_of_element_located((By.XPATH,"//a[text()='Laptops']"))).click()
        wait.until(EC.visibility_of_element_located((By.XPATH,'//div[@class="card-block"]//descendant::a[text()="MacBook Pro"]'))).click()
        
    