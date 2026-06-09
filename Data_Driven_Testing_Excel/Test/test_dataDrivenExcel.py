import pytest
from selenium.webdriver.common.by import By 
from selenium import webdriver
import time
from Utilities import excelReader
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Utilities import logCreator

@pytest.mark.parametrize("username,password",excelReader.get_data("D:\Selenium_Python\Data_Driven_Testing_Excel\ExcelFiles\loginData.xlsx", "Sheet1"))

class TestLogindemo:
     log=logCreator.log_generator()
     def test_validlogin(self,username,password):
        self.driver=webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://www.demoblaze.com/")
        self.log.info("Application Launched")
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable((By.ID, "login2"))).click()
        wait.until(EC.visibility_of_element_located((By.ID, "loginusername"))).send_keys(username)
        wait.until(EC.visibility_of_element_located((By.ID, "loginpassword"))).send_keys(password)
        wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Log in']"))).click()
        self.log.info("Login successfully")
        wait.until(EC.visibility_of_element_located((By.ID, "logout2")))
        logout = self.driver.find_element(By.ID,"logout2")
        assert logout.text == "Log out"
        self.log.info("Assert handled successfull...")
        self.driver.quit()