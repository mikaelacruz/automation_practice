"""UI Automation Practice
Using selenium with python and chrome webdriver
Practicing with https://www.saucedemo.com/ website
Doing basic login and navigation testing"""

from selenium import webdriver
driver = webdriver.Chrome()

# The website I will be navigating to
driver.get("https://www.saucedemo.com/")

assert "sauce" in driver.title

username = driver.find_element_by_id("user-name")
username.clear()
username.send_keys("standard_user")

password = driver.find_element_by_id("password")
password.clear()
password.send_keys("secret_sauce")

login_button = driver.find_element_by_id("login_button").click()
