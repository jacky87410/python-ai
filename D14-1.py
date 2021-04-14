import pandas as pd 
import numpy as np 
df1 = pd.read_csv('https://raw.githubusercontent.com/dataoptimal/posts/master/data%20cleaning%20with%20python%20and%20pandas/property%20data.csv')
print(df1)
df2 = pd.read_csv(
    'https://raw.githubusercontent.com/dataoptimal/posts/master/data%20cleaning%20with%20python%20and%20pandas/property%20data.csv',
    keep_default_na=True,
    na_values=['na', '--']
)
print(df2)
#1.[簡答題] 比較下列兩個讀入的 df 有什麼不同？為什麼造成的？
#其中在SQ_FT那行的--變成NaN，因為df2多了 na_values 自訂缺失值
#2.請將 Dcard API 取得所有的看板資訊轉換成 DataFrame，並且依照熱門程度排序後存成一個 csv 的檔案。
import requests
r = requests.get('https://www.dcard.tw/_api/forums')
response = r.text
import json
data = json.loads(response)
print(data)
n_data = pd.DataFrame(data)
n_data = n_data.sort_values(by = ['subscriptionCount'],ascending = False)
n_data = n_data.drop(['id'],axis = 1)
print(n_data)
n_data.to_csv('data.csv')
