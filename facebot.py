#whatsapp message bot
import getpass
from bs4 import BeautifulSoup
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

password=getpass.getpass(input('password:'))
driver=webdriver.Firefox()
driver.get('http://www.facebook.com')
driver.explicity_wait(5)
name=driver.get_element_by_id("email")
password=driver.get_element_by_id('pass')
name.send_keys('0726956052')
password.send_keys(password)
login=driver.find_element_by_id("u_0_d_lv")

