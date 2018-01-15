from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import json

driver = webdriver.Firefox()
driver.get("https://www.quora.com/")

ids = json.load(open('fieldIds.json'))
userData = json.load(open('userData.json'))

emailId = ids["loginPage"]["email"]
passwordId = ids["loginPage"]["password"]

username = userData["login"]["username"]
password = userData["login"]["password"]

# print(emailId, passwordId, username, password)