from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()

driver.get("http://automationexercise.com")

if(driver.title):
    print("website lanuch successfully")
else:
    print("website lanuch not successfull")

sigin = driver.find_element(by=By.XPATH , value="//a[@href='/login']")
sigin.click()

siginText = driver.find_element(by=By.XPATH ,value="//div[@class='signup-form']/child::h2").text

if(siginText=="New User Signup!"):
    print("New User Signup! is displayed")
else:
    print("not New User Signup! displayed")

name= driver.find_element(by=By.XPATH ,value="//input[@type='text']")
name.send_keys("John")
username=driver.find_element(by=By.XPATH , value="//input[@data-qa='signup-email']")
username.send_keys("John2h2@gmail.com")

driver.find_element(by=By.XPATH ,value="//button[text()='Signup']").click()

signupPage= driver.find_element(by=By.XPATH ,value="//b[text()='Enter Account Information']")

if(signupPage=="Enter Account Information"):
    print("signup page is opened")
else:
    print("signup page is not displayed")

driver.find_element(by=By.XPATH,value="//input[@value='Mr']").click()

driver.find_element(by=By.XPATH,value="//input[@type='password']").send_keys("John@123456")
driver.find_element(by=By.XPATH,value="//input[@name='newsletter']").click()
driver.find_element(by=By.XPATH, value="//input[@name='optin']").click()
driver.find_element(by=By.ID ,value="first_name").send_keys("John")
driver.find_element(by=By.ID,value="last_name").send_keys("Peter")
driver.find_element(by=By.ID,value="company").send_keys("SmartCliff")
driver.find_element(by=By.ID ,value="address1").send_keys("Rs puram")
driver.find_element(by=By.ID ,value="address2").send_keys("Super market")