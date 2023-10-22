from selenium import webdriver
driver=webdriver.Firefox()
driver.get('http://safaricom.zerod.live/zerod-web/p/zerod-home/#/newsfeed/life')
driver.implicitly_wait(10)
head=find_element_by_class_name("zd-body-1")
print(head.text)
