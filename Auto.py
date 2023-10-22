from selenium import webdriver
from selenium.webdriver.common.keys import Keys
driver=webdriver.Firefox()
driver.get("https://safaricom.com/")
print(driver.title)
driver.implicitly_wait(30)
name=driver.find_element_by_xpath("//*[@class='jss28']").text
print(name)

