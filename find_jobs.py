#scarping job posts on The star websites


import pandas as pd 

from selenium import webdriver
import time

title_list=[]
description_list=[]
link_list=[]

driver=webdriver.Firefox()


url="https://www.the-star.co.ke/classifieds/jobs/data-analyst-jobs-in-nairobi.html?p=1&s=default&ei=De6jxx6OIkKIexoFsfi2EA"   
driver.get(url)
title=driver.find_elements_by_xpath("//*[@class='product-title clearfix']")
description=driver.find_elements_by_xpath("//*[@class='product-description']")
link=driver.find_elements_by_xpath("//*[@class='product-source']")
    
   # description=soup.find_all('p',class_="product-description")
    #link=soup.find_all('span',class_="product-source")
for t in title:
      title_list.append(t.text)
for d in description:
      description_list.append(d.text)
for l in link:
     link_list.append(l.text)
        
             

#page_num=driver.find_element_by_xpath("//*[@id='stPgntCrntPg_TA']").text
page_num=1

while int(page_num)!=5:
    
    next_button=driver.find_element_by_link_text('Next Page')
    driver.execute_script("arguments[0].click();", next_button)
    driver.refresh()
    driver.implicitly_wait(15)
    
    #url=f'https://www.the-star.co.ke/classifieds/jobs/data-analyst-jobs-in-nairobi.html?p={str(page_num)}&s=default&ei=vcWgmtqflkutuO4jOyIcuQ'
    #driver.get(url)
    
    title=driver.find_elements_by_xpath("//*[@class='product-title clearfix']")
    
    description=driver.find_elements_by_xpath("//*[@class='product-description']")
    link=driver.find_elements_by_xpath("//*[@class='product-source']")
       
   
    for t in title:
          title_list.append(t.text)
          
    for d in description:
          description_list.append(d.text)
    for l in link:
         link_list.append(l.text)
         
         
    
    page_num+=1
    
dict_jobs={
        'Names':title_list,
        'Description':description_list,
        'Links':link_list
    }
    
range_=[]
for r in range(len(title_list)):
    range_.append(r)

output=pd.DataFrame(dict_jobs,index=range_)
output.to_csv('DataAnalystJobs.csv')
     

print(output)
