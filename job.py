import requests
from bs4 import BeautifulSoup

import csv

url='https://ngodarpan.gov.in/index.php/home/sectorwise_ngo/77031/11/771?per_page=100'
get=requests.get(url).text
soup=BeautifulSoup(get,'html.parser')
table=soup.table
table_data=table.find_all('tr')
for tr in table_data:
    print(tr)

