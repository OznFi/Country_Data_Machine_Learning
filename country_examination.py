# -*- coding: utf-8 -*-
"""
Created on Wed Jul 19 20:59:07 2023

@author: ZBOOK 15 G5
"""
import warnings
import numpy as np
import pandas as pd
import sklearn.mixture as gaussianMixture
from sklearn.experimental import enable_iterative_imputer
from sklearn.impute import IterativeImputer
from sklearn.impute import KNNImputer 

warnings.filterwarnings("ignore", category=FutureWarning)
#pd.set_option('display.max_rows',None)
pd.set_option('display.max_columns',None)

def adjustFeatures(value):
    if(pd.notna(value)):
        if(type(value)!=str):
            value=str(value)
            value = value.replace('$','')
            value = value.replace('%','')
            value = value.replace(',','')
            value = float(value)
        else:
            value = value.replace('$','')
            value = value.replace('%','')
            value = value.replace(',','')
            value = float(value)            
            
        
        
countryData = pd.read_csv('C:/Users/ZBOOK 15 G5/Desktop/country_information.csv')
countryIndexedData = countryData.set_index('Country')
print(countryData.shape)
#there are 195 entries, 35 features
print(countryData.dtypes)

#Features are cleaned of percentages, dollar signs and commas
nonNumericFeatures=['Country','Abbreviation','Capital/Major City','Currency-Code','Largest city','Official language']
for feature in countryData.columns:
    if(feature not in nonNumericFeatures):
        countryData[feature] = countryData[feature].apply(adjustFeatures)
    
     
#print(countryData)
#   countryData[feature]=countryData[feature].astype(str).str.extract(pat='(\d+)',expand=False)

#Removing unrelated values/characters within features

#Finding the features that lack more than 10% of their data    
#nullCounts = countryData.isna().sum()
#print(nullCounts[nullCounts > countryData.shape[0]*0.1])
lacking_features=countryData[['Armed Forces size','Gasoline Price','Minimum wage','Tax revenue (%)']]
non_missing_columns = [col for col in countryData.columns if col not in lacking_features.columns]
print(countryData.columns)

#
#IMPUTATION STEPS START HERE FOR THE LACKING FEATURES
#
lackingFeatureValues = lacking_features.values
nonLackingFeatureValues = countryData.dropna(subset=lacking_features.columns)[countryData.columns].values
nonLackingFeatureValues = countryData.dropna(subset=lacking_features.columns)[['Density','Agricultural Land( %)','Land Area(Km2)','Armed Forces size','Birth Rate','Co2-Emissions','CPI','CPI Change (%)','Fertility Rate','Forested Area (%)','Gasoline Price','GDP','Gross primary education enrollment (%)','Gross tertiary education enrollment (%)','Infant mortality','Life expectancy','Maternal mortality ratio','Minimum wage','Out of pocket health expenditure','Physicians per thousand','Population','Population: Labor force participation (%)','Tax revenue (%)','Total tax rate','Unemployment rate','Urban_population','Latitude','Longitude']]
knnImputer=KNNImputer(n_neighbors = 5)
knn_imputed_features=knnImputer.fit_transform(lackingFeatureValues)

#imputer = IterativeImputer(max_iter=10, random_state=0)
#imputer.fit(nonLackingFeatureValues)

#imputedFeatures = imputer.transform(knn_imputed_features)
#imputedFeatures = pd.DataFrame(imputedFeatures, columns=lacking_features.columns)
print(knn_imputed_features)


#print(lacking_features.describe(include='all'))

#print(lacking_features['Gasoline Price'].head())
#print(lacking_features.describe(include='all'))

