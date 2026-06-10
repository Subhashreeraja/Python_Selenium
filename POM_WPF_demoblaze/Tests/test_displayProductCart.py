import pytest
from  Pages.CartPage import CartPage 
from  Pages.ProductPage import ProductPage 
from Pages.HomePage import HomePage
from selenium import webdriver

@pytest.mark.usefixtures("setup_and_teardown")
class TestDisplayProductCart:
    
 def test_displayProductCart(self):
   homepage = HomePage(self.driver)
   productpage = ProductPage(self.driver)
   homepage.choose_categories_product()
   productpage.click_add_to_cart_btn()
   cartpage = CartPage(self.driver)
   
   expected ="MacBook Pro"
   
   actual=cartpage.verify_product_added_in_the_cart()
   print(actual)
   assert actual == expected
   print("Assert handled successfully...")