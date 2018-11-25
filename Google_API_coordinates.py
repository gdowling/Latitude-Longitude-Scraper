# -*- coding: utf-8 -*-
"""
Created on Mon Nov 19 17:47:30 2018

@author: George
"""
import pandas as pd
import numpy as np
import requests
import json

Locations_file = 'Franchise_Properties.xlsx'
Locations_Sheet = 'Sheet1'
Col_name = 'Hotel Name'

try:
    if Locations_file.split(".")[1] == 'xlsx':
        locations_df = pd.read_excel(Locations_file, sheetname=Locations_Sheet)
        locations_array = np.asarray(locations_df[Col_name])
    elif Locations_file.split(".")[1] == 'csv':
        locations_df = pd.read_csv(Locations_file)
        locations_array = locations_df[Col_name]
except:
    locations_array = np.asarray(Locations_file)
	
content =[]
for loc in locations_array:
    url = 'https://maps.googleapis.com/maps/api/place/textsearch/json?query={}&key=YOUR _GOOGLE_CREDENTIAL'.format(str(loc.replace(' ','+')))
    r = requests.get(url)
    content.append(r.text)

features = ['Property_Name','Address', 'Latitude', 'Longitude']
Complete_df = pd.DataFrame(columns=features)

for i in content:
    loc = json.loads(i)
    for item in loc['results']:
        Property_Name = item['name']
        Address = item['formatted_address']
        Latitude = item['geometry'].get('location').get('lat')
        Longitude = item['geometry'].get('location').get('lng')
        status = item['status']
        location_info = pd.DataFrame([[Property_Name,Address,Latitude,Longitude]])
        location_info.columns = features
        Complete_df = Complete_df.append(location_info, ignore_index = True)

Complete_df.to_csv('Locations_Latitude_Longitude.csv')

