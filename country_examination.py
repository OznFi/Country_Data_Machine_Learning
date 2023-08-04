# -*- coding: utf-8 -*-
"""
Created on Wed Jul 19 20:59:07 2023

@author: ZBOOK 15 G5
"""
import numpy as np
import pandas as pd

countryData = pd.read_csv('C:/Users/ZBOOK 15 G5/Desktop/country_information.csv')
countryIndexedData = countryData.set_index('Country')
nullCounts = countryData.isna().sum()
#print(countryData.shape)
#print(nullCounts[nullCounts > countryData.shape[0]*0.1])
lacking_features=countryData[['Armed Forces size','Gasoline Price','Minimum wage','Tax revenue (%)']]
print(lacking_features.dtypes)
print(lacking_features.tail())
#print(lacking_features.describe(include='all'))
lacking_features['Gasoline Price'] = lacking_features['Gasoline Price'].str.replace('$','').astype(float)
print(lacking_features['Gasoline Price'].head())
#print(lacking_features.describe(include='all'))

