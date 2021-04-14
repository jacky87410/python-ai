import pandas as pd 
import numpy as np 
df1 = pd.DataFrame({
    'fruit': ['apple', 'banana', 'orange'] * 3,
    'weight': ['high', 'medium', 'low'] * 3,
    'price': np.random.randint(0, 15, 9)
})

df2 = pd.DataFrame({
    'fruit': ['apple', 'orange', 'pine'] * 2,
    'weight': ['high', 'low'] * 3,
    'price': np.random.randint(0, 15, 6)
})
# print(df1)
# print(df2)
#1.請接下列資料依照指定規則做合併：
#- 依照 fruit 欄位做合併
print(pd.merge(df1,df2,on = "fruit"))
#- 依照 index 索引做合併
print(df1.join(df2)
# 2.[簡答題] 承上題，請問為什麼依照 merge 合併後有些資料不見了？
#因為用on=fruit做合併，以有共同的fruit做合併所以沒有共同的則會捨棄
#3.[簡答題] 承上題，請問為什麼依照 index 合併會發生錯誤？請用程式解決。
#因為發生索引重疊而未指定
print(pd.concat([df1,df2],axis = 1))