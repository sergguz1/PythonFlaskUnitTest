import time

from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome("chromedriver.exe")
driver.get("https://flaskapptfm.azurewebsites.net/")

@given('I am at the home page')
def step_homepage(self):
    driver.maximize_window()
    time.sleep(10)
    element = ""
    try:
        element = driver.find_element(By.XPATH, "/html/body/div[2]/form/h3").text
    except:
        Exception("Homepage. Element not found")

    if element == "Ingresar":
        print("Step Home page. Value is equal to 'Ingresar', test passed")
        assert True
    else:
        print("Step Home page. Value is NOT equal to 'Ingresar', test failed")
        assert False

@when('I press the Register button')
def step_registerbutton(self):
    try:
        driver.find_element(By.ID, "signUp").click()
        print("Step Register Button, test passed")
        assert True
    except:
        print("Step Register Button, test failed")
        Exception("Register button. Element not found")
        assert False


@Then('I should see the register form')
def step_registerform(self):
    element = ""
    try:
        element = driver.find_element(By.XPATH, "/html/body/div/form/h3").text
    except:
        Exception("Register form. Element not found")

    if element == "Registrarse":
        print("Step Register Form. Value is equal to 'Registrarse', test passed")
        assert True
    else:
        print("Step Register Form. Value is NOT equal to 'Registrarse', test failed")
        assert False
    time.sleep(10)
    driver.close()
