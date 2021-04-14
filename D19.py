import pandas as pd 
import numpy as np 
#題目：運下列時間序列資料做運算
index = pd.date_range('1/1/2019', periods=20, freq='D')
series = pd.Series(range(20), index=index)
print(series)
#1.將所有轉為周資料
print(series.to_period("W"))
#2.將周資料的值取平均
print(series.to_period("W").mean())