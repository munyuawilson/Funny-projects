import selenium
from selenium import webdriver
import requests
from bs4 import BeautifulSoup
choice_library=int(input("Choose either:\n1.Beautiful soup\n2.Selenium\n"))
def beautiful():
    url=input("url>")
    
    
    tag=input('tag_name>')
    choice_selection=int(input('choose what to find \n1.class\n2.id'))
    elements=int(input('1.Single result\n2.Many result'))
    
    if (choice_selection ==1) and (elements==1) :
        class_name=input('input class>')
        soup=BeautifulSoup(requests.get(full_url).text,"html.parser")
        result=soup.find(tag,class_=class_name)
        print(result.text)
    elif (choice_selection ==1) and (elements==2) :
        class_name=input('input class>')
        results=soup.find_all(tag,class_=class_name)
        for r in results:
            print(r)
def selenium_():
    url=input("url>")
    full_url=f'https://{url}'
    
    tag=input('tag_name>')
    choice_selection=int(input('choose what to find \n1.class\n2.id'))
    elements=int(input('1.Single result\n2.Many result'))
    
    if (choice_selection ==1) and (elements==1) :
        class_name=input('input class>')
        driver=webdriver.Firefox()
        driver.get(full_url)
        result=driver.find_element_by_class_name(class_name).text
        print(result)
    
if choice_library == 1:
    beautiful()
elif choice_library == 2:
    selenium_()