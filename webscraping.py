# -*- coding: utf-8 -*-
"""
Created on Fri Oct 16 17:02:40 2020
@author: Vishal
"""

from bs4 import BeautifulSoup as bs
import requests
import pandas as pd


url_to_be_parsed = 'https://en.wikipedia.org/wiki/List_of_brown_dwarfs'

page = requests.get(url_to_be_parsed)
print(page)

soup = bs(page.text,'html.parser')

star_table = soup.find_all('table')

temp_list= []
table_rows = star_table[7].find_all('tr')
for tr in table_rows:
    td = tr.find_all('td')
    row = [i.text.rstrip() for i in td]
    temp_list.append(row)



Star_names = []
Distance =[]
Mass = []
Radius =[]
Lum = []

for i in range(1,len(temp_list)):
    Star_names.append(temp_list[i][1])
    Distance.append(temp_list[i][3])
    Mass.append(temp_list[i][5])
    Radius.append(temp_list[i][6])
    Lum.append(temp_list[i][7])
    
df2 = pd.DataFrame(list(zip(Star_names,Distance,Mass,Radius,Lum)),columns=['Star_name','Distance','Mass','Radius','Luminosity'])
print(df2)

df2.to_csv('brown_dwarfs.csv')