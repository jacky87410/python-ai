import numpy as np 
import pandas as pd     
import seaborn as sns 
import matplotlib.pyplot as plt 
from scipy import stats 
import math
import statistics
#Q1：大樂透的頭獎，你必須從49個挑選出 6 個號碼，且這六個號碼與頭獎的六個號碼一致，頭獎的機率是屬於哪一種分配？
#超幾何分配
#Q2：運用範例的 python 程式碼，計算大樂透的中頭獎機率？
#7.151123842018523e-08
N = 49
K = 6
n = 6
r = 6
probs = stats.hypergeom.pmf(r,N,K,n)
print(probs)
#Q3：你覺得電腦簽注的中獎機率，和人腦簽注相比，哪一個機率高？
#一樣高