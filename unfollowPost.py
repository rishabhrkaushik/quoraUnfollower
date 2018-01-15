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
time.sleep(2)
passwordField[1].send_keys(Keys.ENTER)
time.sleep(10)

print("Login activity complete")

Xpath="//img[contains(@src,'profile_pic_default_small')]"	
navDropdown = driver.find_elements_by_xpath(Xpath)
# print(navDropdown, "\n\n")
menuClick = ActionChains(driver).move_to_element(navDropdown[0]).click().perform()
time.sleep(5)
print("Clicked profile dropdown")

Xpath="//*[contains(@href,'/profile')]"	
navDropdownMenuItems = driver.find_elements_by_xpath(Xpath)
hrefs = [link.get_attribute('href') for link in navDropdownMenuItems]
# print(hrefs)

profileUrl = hrefs[0]
driver.get(profileUrl + "/following")
time.sleep(3)
print("Navigated to following users")

Xpath="//*[contains(@action_click,'UserUnfollow')]"	
followingButtons = driver.find_elements_by_xpath(Xpath)

for followingButton in followingButtons:
	followingButtonClick = followingButton.click()
	time.sleep(0.1)

driver.get(profileUrl + "/topics")
time.sleep(3)

Xpath="//*[contains(@action_click,'TopicUnfollow')]"	
followingButtons = driver.find_elements_by_xpath(Xpath)

for followingButton in followingButtons:
	followingButtonClick = followingButton.click()
	time.sleep(0.1)
time.sleep(5)

driver.get(profileUrl)
time.sleep(10)