from bs4 import BeautifulSoup as bs
import pandas as pd
#from selenium.webdriver.common.by import By
#from selenium import webdriver
import time
import requests

url='https://en.wikipedia.org/wiki/List_of_brown_dwarfs'
#driver=webdriver.Chrome()
#driver.get(url)

time.sleep(10)
scrapped_data=[]

'''def scrap():
    soup=bs(driver.page_source,"html.parser")
    bright_star_table=soup.find_all('table',attrs={'class','wikitable sortable'})
    print(bright_star_table)

scrap()'''

page=requests.get(url)
soup=bs(page.text,'html.parser')
table=soup.find_all('table',{'class':'wikitable sortable'})
total_table=len(table)
print(total_table)
temp_list=[]
table_rows=table[2].find_all('tr')
for tr in table_rows:
    td=tr.find_all('td')
    row=[i.text.rstrip()for i in td]
    temp_list.append(row)
print(temp_list[1])

star_name=[]
distance=[]
mass=[]
radius=[]

for i in range(1,len(temp_list)):
    star_name.append(temp_list[i][0])
    distance.append(temp_list[i][5])
    mass.append(temp_list[i][7])
    radius.append(temp_list[i][8])

headers=['star_name','distance','mass','radius']
df2=pd.DataFrame(list(zip(star_name,distance,mass,radius)),columns=headers)
print(df2)
df2.to_csv('dwarf_stars.csv',index=True,index_label='id')
