# -*- coding: utf-8 -*-
"""
Created on Thu Feb 14 13:44:12 2019

@author: 146790
"""

import os
import pandas as pd
import pickle

os.chdir('D:/Python Text Mining/sms spam')

f=open('SMSSpamCollection',"r",encoding="utf-8")
data=f.read()


sms = pd.read_csv('https://raw.githubusercontent.com/stedy/Machine-Learning-with-R-datasets/master/sms_spam.csv',
                       names= ['label', 'message'])

with open('sms.pickle',mode='wb') as f:
    pickle.dump(sms,f)






