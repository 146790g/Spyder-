# -*- coding: utf-8 -*-
"""
Created on Mon Feb  4 10:34:26 2019

@author: 146790
"""

# -*- coding: utf-8 -*-
"""
Created on Fri Jan 11 14:58:44 2019

@author: 146790
"""

import numpy as np
from scipy import interp
import pandas as pd
import matplotlib.pyplot as plt
import pickle
import os
import nltk


os.chdir('D:\Python Text Mining')
gene=pd.read_csv('genes.csv')
gene2=gene['SYMBOL'].values.tolist()


type(gene2)


with open('df.pickle', mode='rb') as f:
    df=pickle.load(f)

names=df.loc[:,'ID'].values.tolist()
type(names)

dat6=[]

for x in names:
    
    x=names[0]
    string = df.loc[df['ID']==x,'SEN'].values
    len(string)
    type(string)
    a=str(string)
    type(a)
    
    strs=a.lower()
    
    import re
    dat=re.split('[)(#\s]',strs)
            
    dat2=[item for item in dat if item is not '']

    type(dat2)
    type(gene2)


    import numpy as np
    from sklearn.feature_extraction.text import CountVectorizer

    count = CountVectorizer()
    count.fit_transform(dat2)

    dat3=count.vocabulary_

    keys=[]
    dat5={}
    
    for k in dat3.keys():
        keys.append(k.upper())
        values=dat3.values()
        
    dat4 = dict(zip(keys, values))
    select=[w for w in dat4.keys() if w in gene2]
    dat5 = {s:dat4[s] for s in select}

    dat6=dat6.append(dat5)
 
    
