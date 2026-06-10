import pytest
from  Pages.CartPage import CartPage 
from  Pages.ProductPage import ProductPage 
from Pages.HomePage import HomePage
from selenium import webdriver
from Utilities import log_creator
@pytest.mark.usefixtures("setup_and_teardown")
class TestDisplayProductCart:
    
 def test_displayProductCart(self):
   self.log=log_creator.log_generator()
   homepage = HomePage(self.driver)
   productpage = ProductPage(self.driver)
   homepage.choose_categories_product()
   productpage.click_add_to_cart_btn()
   cartpage = CartPage(self.driver)
   
   expected ="MacBook Pro"
   
   actual=cartpage.verify_product_added_in_the_cart()
   assert actual == expected
   self.log.info("Assert handled successfully...")