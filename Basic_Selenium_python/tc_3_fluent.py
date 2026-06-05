from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException

driver = webdriver.Chrome()
print("Chrome is assigned")


wait = WebDriverWait(
    driver,
    timeout=20,
    poll_frequency=0.5,
    ignored_exceptions=[NoSuchElementException]
)

driver.maximize_window()
driver.get("https://automationexercise.com/")

home_element = driver.find_element(By.XPATH,"//a[normalize-space()='Home']")
wait.until(EC.visibility_of(home_element))

if home_element.is_displayed():
    print("Home page is visible")
else:
    print("Home page is not visible")

login_button = driver.find_element(By.XPATH,"//a[text()=' Signup / Login']")
wait.until(EC.visibility_of(login_button))
login_button.click()

login_text = driver.find_element(By.XPATH,"//div[@class='col-sm-4 col-sm-offset-1']//descendant::h2")
wait.until(EC.visibility_of(login_text))

if login_text.is_enabled():
    print("Login to your account is visible")
else:
    print("Login to your account is not visible")

email_field = driver.find_element(By.XPATH,'//form[@method="POST"]//child::input[@data-qa="login-email"]')
wait.until(EC.visibility_of(email_field))
email_field.send_keys("Subhashree@gmail.com")
print("wrong email passed")

password_field = driver.find_element(By.XPATH,'//form[@method="POST"]//child::input[@data-qa="login-password"]')
wait.until(EC.visibility_of(password_field))
password_field.send_keys("sghjk")
print("wrong password passed")

button = driver.find_element(By.XPATH,"//button[@data-qa='login-button']")
wait.until(EC.element_to_be_clickable(button))
button.click()
print("button is clicked")

error_msg = driver.find_element(By.XPATH,'//input[@data-qa="login-password"]//following::p[text()="Your email or password is incorrect!"]')
wait.until(EC.visibility_of(error_msg))

if error_msg.is_displayed():
    print("error msg is visible")
else:
    print("error msg is not visible")


driver.close()    