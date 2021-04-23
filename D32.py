import numpy as np 
import pandas as pd 
import seaborn as sns 
import matplotlib.pyplot as plt 
import math 
from scipy import stats
import statistics
#Q1：計算標準常態分配，小於 1 的機率有多大？
#0.8413447460685429
x = stats.norm.cdf(1,0,1)
print(x)
#Q2：計算標準常態分配，大於1，小於 -1 的機率有多大？
#0.15865525393145707
x = stats.norm.cdf(-1,0,1)
print(x)
#Q3：X~N(2,4),x 服從常態分配，平均數為2,變異數為 4，計算 X小於 6 的機率有多大?
#0.9772498680518208
mu = 2
sigma = 2
y = stats.norm.cdf(6,mu,sigma)
print(y)