import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt
#題目 : 將資料夾中 boston.csv 讀進來，並用圖表分析欄位。
bos_data = pd.read_csv("boston.csv")
#1.畫出箱型圖，並判斷哪個欄位的中位數在 300~400 之間？
#TAX
bos_data.boxplot()
plt.show()
#2.畫出散佈圖 x='NOX', y='DIS' ，並說明這兩欄位有什麼關係？
#NOX與DIS成反向關係 一個越大另一個就越小
bos_data.plot.scatter(x="NOX",y="DIS")
plt.show()