import numpy as np 
import pandas as pd 
import math  
import seaborn as sns 
import matplotlib.pyplot as plt 
import statistics
from scipy import stats
import statsmodels.stats.proportion
#作業 1：用 A/B test 幫工廠做決定吧
#某工廠想知道兩條不同的生產線的產品不良率是否有所不同，由兩條生產線中各抽取 300 個樣本，第一組有 75 個不良品，第二組有 30 個不良品，我們可以宣稱生產線所生產出的產品不良率不相同？(以0.05 為顯著水準)？
#(提示：透過課程投影片的步驟，需思考 H0、H1 的寫法範例不同唷。)
#HO:生產線的產品不良率相同
#H1:生產線的產品不良率不同
A = [75,30]
B = [300,300]
r = statsmodels.stats.proportion.proportions_ztest(A,B,alternative = 'two-sided')
print(r[1])
#P-value小於0.05拒絕虛無假設，所以兩生產線產品不良率不同
#作業 2：你的工作，有需要 A/B test 幫你做決定？
#不需要
#可以在論壇中，寫出你的問題，嘗試用今天課程教的方法，透過 5個步驟的拆解，計算出結果，透過統計輔助你做決策。
