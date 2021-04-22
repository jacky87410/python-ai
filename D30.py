import numpy as np 
import pandas as pd 
import seaborn as sns 
import matplotlib.pyplot as plt 
from scipy import stats
#機率可以怎麼用？
#丟一個銅板，丟了100次，出現正面 50 次的機率有多大。
#(提示：先想是哪一種分配，然後透過 python 語法進行計算)
#0.07958923738717888
p = 0.5
n = 100
r = 50
probs = stats.binom.pmf(r,n,p)
print(probs)