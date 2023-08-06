# -*- coding: utf-8 -*-
"""
Created on Wed Jul 19 20:59:07 2023

@author: ZBOOK 15 G5
"""
import warnings
import numpy as np
import pandas as pd

warnings.filterwarnings("ignore", category=FutureWarning)
#pd.set_option('display.max_rows',None)
pd.set_option('display.max_columns',None)

countryData = pd.read_csv('C:/Users/ZBOOK 15 G5/Desktop/country_information.csv')
countryIndexedData = countryData.set_index('Country')
print(countryData.shape)
#there are 195 entries, 35 features
print(countryData.dtypes)

nonNumericFeatures=['Country','Abbreviation','Capital/Major City','Currency-Code','Largest city','Official language']
for feature in countryData.columns:
    if(feature not in nonNumericFeatures):
        countryData[feature] = countryData[feature].str.replace('$','')
        countryData[feature] = countryData[feature].str.replace('%','')
        countryData[feature] = countryData[feature].str.replace(',','')
        countryData[feature] = countryData[feature].astype(float)
    
     
#print(countryData)
#   countryData[feature]=countryData[feature].astype(str).str.extract(pat='(\d+)',expand=False)

#Removing unrelated values/characters within features
countryData['Gasoline Price'] = countryData['Gasoline Price'].str.replace('$','').astype(float)
countryData['Minimum wage'] = countryData['Minimum wage'].str.replace('$','').astype(float)
countryData['Tax revenue (%)'] = countryData['Tax revenue (%)'].str.replace('%','').astype(float)

nullCounts = countryData.isna().sum()
#print(nullCounts[nullCounts > countryData.shape[0]*0.1])
#The missing data threshold is taken as 10%

lacking_features=countryData[['Armed Forces size','Gasoline Price','Minimum wage','Tax revenue (%)']]
#print(lacking_features.dtypes)
#print(lacking_features.tail())
#print(lacking_features.describe(include='all'))

#print(lacking_features['Gasoline Price'].head())
#print(lacking_features.describe(include='all'))

