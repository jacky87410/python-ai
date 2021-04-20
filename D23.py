import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns
#作業目標：
#繪製模型殘差 圖進一步了解不同的特徵值所呈現的關係圖 
#1.顯示的四個變數中, 把hue 套用 sex
#x="total_bill", y="tip", hue="sex", style="time"
tips = sns.load_dataset("tips")
fmri = sns.load_dataset("fmri")
print(tips.head())
sns.relplot(x = "total_bill",y = "tip",hue = "sex",style ="time",data = tips )
plt.show()
#2.使用新的數據集fmri, 再跑一次
print(fmri.head())
sns.relplot(x = "timepoint",y='signal',hue = 'event',style = 'region',data = fmri)
plt.show()
sns.regplot(x = "timepoint",y = "signal",data = fmri)
plt.show()
