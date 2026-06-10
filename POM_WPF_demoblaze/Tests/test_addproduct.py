import pytest
from  Pages.ProductPage import ProductPage 
from Pages.HomePage import HomePage
from selenium import webdriver

@pytest.mark.usefixtures("setup_and_teardown")
class TestAddProduct:
    
 def test_addProduct(self):
   homepage = HomePage(self.driver)
   productpage = ProductPage(self.driver)
   homepage.choose_categories_product()
   expected ="Product added"
   
   actual=productpage.click_add_to_cart_btn()
   print(actual)
   assert actual == expected
   print("Assert handled successfully...")