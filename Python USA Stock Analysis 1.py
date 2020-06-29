# -*- coding: utf-8 -*-
"""
Created on Wed Dec 26 20:35:25 2018

@author: maete
"""
from pandas_datareader import data

import matplotlib.pyplot as plt
import pandas as pd
import datetime as dt
import numpy as np
import os

import csv

os.getcwd()

os.chdir("D:\Python US Stocks\Data")

symbol=pd.read_csv('symbol2.csv',header=None)

type(symbol)

symbol.head()

symbol2=symbol.iloc[:,0]
tickerList=symbol2.values.tolist()

type(symbol2)



# 期間設定
start = dt.date(2013,1,1)
end = dt.date(2017,12,31)
 
# ダウンロードリスト
tickerList = ['AMZN','AMBA','BA','CSCO','NVDA','PFE','PM','VYM']
 
# ダウンロードリストを一括ダウンロード
stock = data.DataReader(tickerList,'yahoo',start,end)
 
stock.head()

