# -*- coding: utf-8 -*-
"""
Created on Wed Feb 13 10:55:02 2019

@author: 146790
"""

import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.datasets import fetch_20newsgroups
import os

news20 = fetch_20newsgroups()

type(news20)

os.chdir('C:\')

os.chdir(　r'C:\)

os.chdir("C:\Python\KUJIRA")

    os.getcwd()

a=[1,2,3]

import pickle
with open('news20t.pickle', mode='wb') as fp:
    pickle.dump(news20, fp)
    
    
sample_list = [1,2,3]
f = open('sample.textfile','wb')
pickle.dump(sample_list,f)
    
    

vectorizer = TfidfVectorizer(min_df=0.03)
tfidf_X = vectorizer.fit_transform(news20.data[:1000]).toarray() 