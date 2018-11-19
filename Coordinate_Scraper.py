# -*- coding: utf-8 -*-
"""
Created on Sun Nov 18 16:13:16 2018

@author: George
"""
import pandas as pd
import numpy as np
import requests
from bs4 import BeautifulSoup

Locations_file = 'Locations _to_lookup.xlsx'
Locations_Sheet = 'Sheet1'
Col_name = 'Locations'

try:
    if Locations_file.split(".")[1] == 'xlsx':
        locations_df = pd.read_excel(Locations_file, sheetname=Locations_Sheet)
        locations_array = np.asarray(locations_df[Col_name])
    elif Locations_file.split(".")[1] == 'csv':
        locations_df = pd.read_csv(Locations_file)
        locations_array = locations_df[Col_name]
except:
    locations_array = np.asarray(Locations_file)
    
features = ['Location', 'Latitude', 'Longitude']
Complete_df = pd.DataFrame(columns=features)
    
for loc in locations_array:
    desired_location = loc
    search_url = 'https://www.google.com/search?q='
    url = search_url + str(desired_location.replace(' ','+'))
    r = requests.get(url)
    content = r.text
    soup = BeautifulSoup(content)
    body = soup.find('body')
    map_class = body.find('a',{'class' :'qrSWbe KDZjCd'},  
                          href=lambda href: href and "maps" in href)
    map_url = map_class.get('href')
    r_map = requests.get(map_url)
    content_map = r_map.text
    soup_map = BeautifulSoup(content_map)
    head = soup_map.find('head')
    url_long_lat = head.find_all('meta')[8].get('content')
    Lat, Long = url_long_lat[url_long_lat.find('center=')+
                         len('center='):url_long_lat.rfind('&zoom')].split('%2C')
    location_info = pd.DataFrame([[desired_location,Lat,Long]])
    location_info.columns = features
    Complete_df = Complete_df.append(location_info, ignore_index = True)
    
Complete_df.to_csv('Locations_Latitude_Longitude.csv')
           

