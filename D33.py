import numpy as np 
import pandas as pd 
import seaborn as sns
import matplotlib.pyplot as plt 
from scipy import stats 
import math 
import statistics
def bayes_theorem(p_a,p_b_given_a,p_b_given_not_a):
    not_a = 1 - p_a
    p_b = p_b_given_a * p_a + p_b_given_not_a * not_a
    p_a_given_b = (p_b_given_a * p_a)/p_b
    return p_a_given_b
#Q1：所以根據這個情況條件下。你會預測照片中的長髮是男性或女性？ (直覺回答)
#女生
#Q2：以下圖資料，計算當你看到長髮時，是女生的機率？
#0.35714285714285715
p_a = 0.1
p_b_given_a = 0.5
p_b_given_not_a = 0.1
result = bayes_theorem(p_a,p_b_given_a,p_b_given_not_a)
print(result)
#Q3：你的決策因為男生女生比例不同 (先驗分配不同)，決策有沒有改變？
#有



