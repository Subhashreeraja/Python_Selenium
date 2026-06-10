import pytest
from  Pages.ProductPage import ProductPage 
from Pages.HomePage import HomePage
from selenium import webdriver
from Utilities import log_creator
@pytest.mark.usefixtures("setup_and_teardown")
class TestAddProduct:
    
 def test_addProduct(self):
   log=log_creator.log_generator()
   homepage = HomePage(self.driver)
   productpage = ProductPage(self.driver)
   homepage.choose_categories_product()
   expected ="Product added"
   
   actual=productpage.click_add_to_cart_btn()
   self.log.info(actual)
   assert actual == expected
   self.log.info("Assert handled successfully...")