# -*- coding: utf-8 -*-
"""
Created on Mon Jul 20 11:46:08 2020

@author: erick
"""

import pandas as pd
import numpy as np
df = pd.read_csv('movies_metadata.csv')


print("Columns of the DataFrame:")
print(df.columns)
third_movie = df.iloc[2]

print("Details of the third moviee:")
print(third_movie)

result = df.shape
print("Number of rows and columns of the DataFrame:")
print(result)
