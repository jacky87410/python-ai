import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns 
from scipy import stats
import math 
import statistics  
boys=[164, 176, 169, 169, 165, 175, 159, 151, 144, 160, 183, 165, 156, 170,
 164, 173, 165, 163, 177, 171]
girls = [169, 170, 162, 154,
        183, 173, 169, 167,
        170, 185, 162, 175,
        168, 151, 181, 170,
        182, 156, 159, 160]
#作業1 (程式&觀察&思考題)：
#為了了解台灣男生和女生在身高上誰比較高，收集到 20位男生和20位女生的身高。資料如下：
#在 google 表單中，寫下答案。
#Q1：試著用今天所教的內容，如何描述這兩組資料的樣態？
print("男孩身高平均=",np.mean(boys))
print("女孩身高平均=",np.mean(girls))
print("男孩身高中位數=",np.median(boys))
print("女孩身高中位數=",np.median(girls))
print("男孩身高眾數=",stats.mode(boys))
print("女孩身高眾數=",stats.mode(girls))
def rangeV(x): 
  return(max(x)-min(x))
print("男孩身高全距",rangeV(boys))
print("女孩身高全距",rangeV(girls))
print("男孩身高變異數=",np.var(boys,ddof=1))
print("女孩身高變異數=",np.var(girls,ddof=1))
print("男孩身高標準差=",np.std(boys))
print("女孩身高標準差=",np.std(girls))
print("男生90百分位數=",np.percentile(boys, 90))
print("男生50百分位數=",np.percentile(boys, 50))
print("男生20百分位數=",np.percentile(boys, 20))
print("女生90百分位數=",np.percentile(girls, 90))
print("女生50百分位數=",np.percentile(girls, 50))
print("女生20百分位數=",np.percentile(girls, 20))
print('男生身高峰度',stats.skew(boys))
print('男生身高偏度',stats.kurtosis(boys))
print('女生身高峰度',stats.skew(girls))
print('女生身高偏度',stats.kurtosis(girls))
#Q2：請問男生和女生在平均身高上誰比較高？
#女生
#Q3：請問第二題的答案和日常生活中觀察的一致嗎？如果不一致，你覺得原因可能為何？
#不一致
#請將上述答案，填寫在 google 表單中。