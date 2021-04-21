import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns
#作業: 取得另一個 dataset: titanic, tips
df = sns.load_dataset("titanic")
print(df.info())
#(1) 做條形圖
print(df.head())
sns.barplot(x = "sex",y="survived",hue = "class",data = df)
plt.show()
#(2) 異常值落點分析
df = sns.load_dataset("tips")
print(df.info())
print(df.head())
sns.boxplot(x="sex",y = "total_bill",data=df)
sns.stripplot(x="sex",y="total_bill",data = df)
plt.show()