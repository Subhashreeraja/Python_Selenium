import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


@pytest.fixture(scope="module")
def driver():

    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(10)
    yield driver
    driver.quit()

@pytest.mark.order(1)
@pytest.mark.dependency(name="login")
def test_login(driver):

    driver.get("https://tutorialsninja.com/demo/")

    driver.find_element(By.XPATH, "//span[text()='My Account']").click()
    driver.find_element(By.LINK_TEXT, "Login").click()

    driver.find_element(By.ID, "input-email").send_keys("priyamurugesan@gmail.com")
    driver.find_element(By.ID, "input-password").send_keys("1234")
    driver.find_element(By.XPATH, "//input[@value='Login']").click()

    assert "My Account" in driver.page_source



@pytest.mark.order(2)
@pytest.mark.dependency(name="search", depends=["login"])
def test_search_product(driver):

    search_box = driver.find_element(By.NAME, "search")
    search_box.clear()
    search_box.send_keys("iPhone")
    search_box.send_keys(Keys.ENTER)

    product = driver.find_element(By.LINK_TEXT, "iPhone")

    assert product.is_displayed()




@pytest.mark.order(3)
@pytest.mark.dependency(name="cart", depends=["search"])
def test_add_to_cart(driver):

    driver.find_element(By.LINK_TEXT, "iPhone").click()

    driver.find_element(By.ID, "button-cart").click()

    success_message = driver.find_element(
        By.CSS_SELECTOR,
        ".alert-success"
    )

    assert success_message.is_displayed()


@pytest.mark.order(4)
@pytest.mark.dependency(depends=["cart"])
def test_logout(driver):

    driver.find_element(By.XPATH, "//span[text()='My Account']").click()
    driver.find_element(By.LINK_TEXT, "Logout").click()

    assert "Account Logout" in driver.page_source