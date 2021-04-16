import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 
df =pd.read_csv("boston.csv")
df = pd.DataFrame(df)
print(df.head())
#題目 : 將資料夾中 boston.csv 讀進來，並用圖表分析欄位。
#1.畫出箱型圖，並判斷哪個欄位的中位數在 300~400 之間？
#key B欄位的中位數介於300~400
plt.boxplot(df)
plt.show()
print(df.columns[10],df.columns[12])
#2.畫出散佈圖 x='NOX', y='DIS' ，並說明這兩欄位有什麼關係？
#兩個欄位成反比，即一邊大另一邊就會小
x = df["NOX"]
y = df["DIS"]
plt.scatter(x,y)
plt.show()