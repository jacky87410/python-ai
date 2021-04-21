import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns 
import os
os.getcwd()
df_red = pd.read_csv("winequality_red.csv")
df_white = pd.read_csv("winequality_white.csv")
df_red["color"] = "R"
df_white['color'] = "W"
df_all = pd.concat([df_red,df_white],axis=0)
print(df_all.head())
df_all.rename(columns = {'fixed acidity': 'fixed_acidity','citric acid':'citric_acid',
                       'volatile acidity':'volatile_acidity','residual sugar':'residual_sugar',
                       'free sulfur dioxide':'free_sulfur_dioxide',
                       'total sulfur dioxide':'total_sulfur_dioxide'},inplace = True)
print(df_all.head())
sns.histplot(df_all['quality'])
plt.show()
df = pd.get_dummies(df_all,columns = ["color"])
df_all.isnull().sum()
print(df_all.info())
print(df_all.describe())
df_all.hist(bins=10,color="lightblue",edgecolor='blue',linewidth=1.0,xlabelsize=8,ylabelsize=8,grid=False)
plt.tight_layout(rect = (0,0,1.2,1.2))
plt.show()
#作業(1)：更改 df_all.hist 裡面 bins 的參數值，看看資料分布的變化
df_all.hist(bins=15,color="lightblue",edgecolor='blue',linewidth=1.0,xlabelsize=8,ylabelsize=8,grid=False)
plt.tight_layout(rect = (0,0,1.2,1.2))
plt.show()
#作業(2)：延伸 作業(1)，更改 df_all.hist 裡面 grid 的參數值，看看版面的變化
df_all.hist(bins=15,color="lightblue",edgecolor='blue',linewidth=1.0,xlabelsize=8,ylabelsize=8,grid=True)
plt.tight_layout(rect = (0,0,1.2,1.2))
plt.show()
#作業(3)：更改 plt.tight_layout(rect=(x1, y1, x2, y2)), x / y 值 看看版面的變化
df_all.hist(bins=15,color="lightblue",edgecolor='blue',linewidth=1.0,xlabelsize=8,ylabelsize=8,grid=False)
plt.tight_layout(rect = (0,0,1,1))
plt.show()