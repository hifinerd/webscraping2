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



Brown_dwarf = []
Constellation =[]
Right_ascension = []
Declination =[]
App_mag = []
Distance = []
Spectral_type = []
Mass = []
Radius = []
Discovery_year = []

for i in range(1,len(temp_list)):
    Brown_dwarf.append(temp_list[i[1]])
    Constellation.append(temp_list[i[2]])
    Right_ascension.append(temp_list[i[3]])
    Declination.append(temp_list[i[4]])
    App_mag.append(temp_list[i[5]])
    Distance.append(temp_list[i[6]])
    Spectral_type.append(temp_list[i[7]])
    Mass.append(temp_list[i[8]])
    Radius.append(temp_list[i[9]])
    Discovery_year.append(temp_list[i[10]])
    
df2 = pd.DataFrame(list(zip(Brown_dwarf, Constellation, Right_ascension, Declination, App_mag, Distance, Spectral_type, Mass, Radius, Discovery_year)),columns=['Brown_dwarf', 'Constellation' 'Right_ascension', 'Declination', 'App_mag', 'Distance', 'Spectral_type', 'Mass', 'Radius', 'Discovery_year'])
print(df2)

df2.to_csv('brown_dwarfs.csv')