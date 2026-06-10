import pytest
from  Pages.HomePage import HomePage 
from selenium import webdriver
from Utilities import read_config
from Utilities import log_creator
@pytest.mark.usefixtures("setup_and_teardown")
class TestLogin:
    
 def test_login(self):
   log=log_creator.log_generator()
   homepage = HomePage(self.driver)
   username=read_config.get_config("Login Credentials","username")
   password=read_config.get_config("Login Credentials","password")
   homepage.login(username,password)
   
   expected = f"Welcome {username}"
   self.log.info(expected)
   actual= homepage.verify_welcome_msg()
   assert actual == expected
   self.log.info("Assert handled successfully...")
   
   

