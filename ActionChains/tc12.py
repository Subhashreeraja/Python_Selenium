import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

def dismiss_ads(driver):
    try:
        driver.execute_script("""
            var iframes = document.querySelectorAll('iframe');

            for (var i = 0; i < iframes.length; i++) {
                var src = iframes[i].src || '';
                var id = iframes[i].id || '';

                if (
                    src.includes('doubleclick') ||
                    src.includes('googleads') ||
                    src.includes('googlesyndication') ||
                    id.includes('aswift') ||
                    id.includes('google_ads')
                ) {
                    iframes[i].remove();
                }
            }
        """)
        print("Ads dismissed")

    except Exception as e:
        print(f"Ad dismissal skipped: {e}")
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://automationexercise.com/")
dismiss_ads(driver)



home_element=driver.find_element(By.XPATH,"//a[normalize-space()='Home']")
if home_element.is_displayed():
    print("Home page is visible")
else:
    print("Home page is not visible")  

product_button=driver.find_element(By.XPATH,'//div[@class="shop-menu pull-right"]//a[@href="/products"]') 
product_button.click()
dismiss_ads(driver)

driver.execute_script("window.scrollBy(0, 500);")
   
actions = ActionChains(driver)   
first_product=driver.find_element(By.XPATH,'//div[@class="product-image-wrapper"]//child::img[@src="/get_product_picture/1"]')
actions.move_to_element(first_product).perform()
cart_btn=driver.find_element(By.XPATH,"//div[@class='overlay-content']//child::a[@data-product-id='1']")   
hover_value=driver.find_element(By.XPATH,'//a[@data-product-id="1"]//ancestor::div[@class="product-overlay"]')
hover=hover_value.value_of_css_property("display")
assert hover=="block","hover is not applied"
print("hover is applied")
time.sleep(5)
actions.move_to_element(cart_btn).click().perform()
print("clicked the cart btn")
time.sleep(10)


