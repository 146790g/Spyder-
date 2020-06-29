# -*- coding: utf-8 -*-
"""
Created on Fri Feb  8 10:08:33 2019

@author: 146790
"""

import pandas as pd
import os

os.chdir('D:\Python Text Mining')

df = pd.read_csv(filepath_or_buffer="docs3.csv", encoding="ms932", sep=",")

type(df)

df.shape
df.index
df.columns

df=df.drop('Unnamed: 0',axis=1)

with open('df.pickle',mode='wb') as f:
    pickle.dump(df,f)





