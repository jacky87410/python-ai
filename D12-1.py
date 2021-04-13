import pandas as pd 
import numpy as np 
data = {'animal': ['cat', 'cat', 'snake', 'dog', 'dog', 'cat', 'snake', 'cat', 'dog', 'dog'],
        'age': [2.5, 3, 0.5, np.nan, 5, 2, 4.5, np.nan, 7, 3],
        'visits': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
        'priority': ['yes', 'yes', 'no', 'yes', 'no', 'no', 'no', 'yes', 'no', 'no']}

labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

df = pd.DataFrame(data, index=labels)
print(df)
#1.根據給定的 DataFrame 中取出索引為 3, 4, 8 的 animal 和 age 欄位。
#索引3：animal - dog age - nan
#索引4：animal - dog age - 5.0
#索引8：animal - dog age - 7.0
for i in range(len(df)):
        if  i == 3 or i==4 or i==8:
                print(df.animal[i])
                print(df.age[i])
#2.請將 dataFrame 所有字串都變成是大寫開頭。
df = pd.DataFrame([
    ['tom', 'mark', 'mary'],
    ['bob', 'alice', 'john']
])
print(df)
df[0] = df[0].str.title()
df[1] = df[1].str.title()
df[2] = df[2].str.title()
print(df)