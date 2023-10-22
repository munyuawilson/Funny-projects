#scrap the notice board of karu
from tkinter import *
import pandas as pd
import csv

from bs4 import BeautifulSoup
import requests
import lxml
url="https://karu.ac.ke/student-notice-board/"
get=requests.get(url).text
content=BeautifulSoup(get,'html.parser')
w=content.find('h3',class_="gdlr-core-blog-title gdlr-core-skin-title").a


ntitles=content.find_all('h3',class_="gdlr-core-blog-title gdlr-core-skin-title")
for w in ntitles:
    
    b=w.text
    print(b)
    with open('notice.txt','w') as file:
       file.write(b)
       file.close()

        