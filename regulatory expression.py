# -*- coding: utf-8 -*-
"""
Created on Fri Feb  8 16:03:21 2019

@author: 146790
"""

import re
import pandas as pd
 
# 対象の文字列
text = "abc123def456efg"
 
# 連続した小文字のアルファベットを置換
result1 = re.sub(r'[a-z]+', "0", text)

print(result1)

result2 = re.sub(r'[a-z]', "0", text)

print(result2)

docs = np.array([
        'The &%%!! sun /// is ** ☆ shining )() ??>',
        'The weather is sweet',
        'The sun is shining, the weather is sweet, and one and one is two'])

df=pd.DataFrame(docs)

df.shape

def preprocessor(text):
    text=re.sub('[\W]+',' ',text.lower())
    print(text)

preprocessor(str(df.iloc[0,0]))



