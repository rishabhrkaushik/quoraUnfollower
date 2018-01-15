from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import json
import time

driver = webdriver.Firefox()
driver.get("https://www.quora.com/")

userData = json.load(open('userData.json'))

username = userData["login"]["username"]
password = userData["login"]["password"]

# print( username, password)
Xpath="//input[contains(@id,'_email')]"	
emailField = driver.find_elements_by_xpath(Xpath)
emailField[1].send_keys(username)

Xpath="//input[contains(@id,'_password')]"	
passwordField = driver.find_elements_by_xpath(Xpath)
passwordField[1].send_keys(password)
time.sleep(5)
passwordField[1].send_keys(Keys.ENTER)
time.sleep(5)

print("Login activity complete")
