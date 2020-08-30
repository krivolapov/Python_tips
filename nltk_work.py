# -*- coding: utf-8 -*-
"""
Created on Tue Aug 18 08:29:56 2020

@author: Max
"""

# load modules
import json
import pandas as pd
import numpy as np
from sklearn import datasets, cluster
import matplotlib.pyplot as plt

# read out JSON file
with open('posts_with_topics.json') as f:
      data = json.load(f)
#print(data)

df = pd.read_json('posts_with_topics.json')

json_string = json.dumps(data)

new_df = df["topics"]

features_df = pd.DataFrame(new_df.explode().value_counts())

list_of_features = pd.Series(features_df.index.to_list())

df_all_features = pd.DataFrame(columns=list_of_features, dtype = 'int')

for i in range(len(new_df)):
    for j in range(len(list_of_features)):
        df_all_features.loc[i, list_of_features[j]] = int(list_of_features[j] in new_df[i])
        

#ax = features_df.plot.barh(figsize=(20,50)) 

# df_all_features.iloc[[0]]       
# vector_prod = vector.T.dot(vector)

for i in range(len(df_all_features)):
    appearance_df = appearance_df + df_all_features.iloc[[i]].T.dot(df_all_features.iloc[[i]])
    
appearance_df_norm = appearance_df.div(features, axis = 0)