import pytest
import read_config
import time
from selenium.webdriver.common.by import By
@pytest.mark.usefixtures("test_setup_and_teardown")
class TestLogin:
    def test_valid_login(self):
       self.driver.find_element(By.XPATH,"//a[@id='login2']").click()
       username=read_config.get_config("Login Credentials","user")
       password=read_config.get_config("Login Credentials","pass")
       self.driver.find_element(By.XPATH,"//input[@id='loginusername']").send_keys(username)
       self.driver.find_element(By.XPATH,"//input[@id='loginpassword']").send_keys(password)
       self.driver.find_element(By.XPATH,"//button[normalize-space()='Log in']").click()
       
    def test_invalid_login(self):
       self.driver.find_element(By.XPATH,"//a[@id='login2']").click()
       username=read_config.get_config("Invalid Credentials","user")
       password=read_config.get_config("Invalid Credentials","pass")
       self.driver.find_element(By.XPATH,"//input[@id='loginusername']").send_keys(username)
       self.driver.find_element(By.XPATH,"//input[@id='loginpassword']").send_keys(password)
       self.driver.find_element(By.XPATH,"//button[normalize-space()='Log in']").click()
       time.sleep(5)
       alert = self.driver.switch_to.alert
       actual_msg = alert.text
       expected_msg = "User does not exist."
       assert actual_msg == expected_msg
       alert.accept()
       
       
       
       
       
       
       
       
       
       
    