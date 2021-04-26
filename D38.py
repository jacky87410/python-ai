import numpy as np 
import pandas as pd 
import math  
import statistics
from scipy import stats
import matplotlib.pyplot as plt 
import seaborn as sns 
df_train = pd.read_csv("Titanic_train.csv")
#在鐵達尼資料集中，可以用今天範例中提到的三種辨識異常值的方法，以 training data 為資料集。
#Q1：觀察票價是否有異常值的現象？
#有異常值
print(df_train["Fare"].describe())
#Q2：你覺得找出的異常需要做處理嗎？ (可以試著講出自己的想法)
#不一定 要看異常值變數去做決定