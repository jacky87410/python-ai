import numpy as np 
import pandas as pd 
import math 
import seaborn as sns 
import matplotlib.pyplot as plt 
import statistics 
from scipy import stats 
from IPython.display import display
import sklearn 
pd.set_option('display.max_columns',None)
pd.set_option('display.max_rows',None)
pd.set_option('max_colwidth',100)
import pingouin as pg 
import researchpy   
df_train = pd.read_csv("Titanic_train.csv")
print(df_train.info())
df_train['Survived_cate']=df_train['Survived']
df_train['Survived_cate']=df_train['Survived_cate'].astype('object')
print(df_train.info())
complete_data=df_train[['Age','Survived_cate','Sex']].dropna()
display(complete_data)
#在鐵達尼資料集中，今天我們專注觀察變數之間的相關性，以 Titanic_train.csv 中，首先將有遺失值的數值刪除，我們取 Titanic_train.csv 的年齡資料，試著將課堂中所學的方法應用上去。
#@Q1：產生一個新的變數 (Age_above65_)  Age ≧ 65 為 'Y'，其餘為 'N'。  
def Age_above65_(x):
    if(x >= 65):
        return("Y")
    else:
        return('N')
complete_data['age_category']=complete_data['Age'].apply(Age_above65_)
#Q2：將性別 (sex) 一併列入考慮，產生一個新的變數(Age_above65_female)，當 sex = female 或Age>=65為'Y'，其餘為'N'。
def female65(df):
    if df['age_category'] == "Y" or df['Sex'] == "female":
        return "Y"
    else:
        return "N"
complete_data['Age_above65_female'] = complete_data.apply(female65, axis=1)
#Q3：透過昨天課程的內容，驗證產生的兩個新變數，哪一個和目標變數(Survived_cate) 的相關性較高？
#Age_above65_female和Survived_cate相關性較高
conttable = pd.crosstab(complete_data['Survived_cate'], complete_data['age_category'])
df1 = min(conttable.shape[0], conttable.shape[1]) - 1
crosstab1, res1 = researchpy.crosstab(complete_data['Survived_cate'], complete_data['age_category'], test='chi-square')
print(res1)

def judgment_CramerV(df,V):
    if df == 1:
        if V < 0.10:
            qual = 'negligible'
        elif V < 0.30:
            qual = 'small'
        elif V < 0.50:
            qual = 'medium'
        else:
            qual = 'large'
    elif df == 2:
        if V < 0.07:
            qual = 'negligible'
        elif V < 0.21:
            qual = 'small'
        elif V < 0.35:
            qual = 'medium'
        else:
            qual = 'large'
    elif df == 3:
        if V < 0.06:
            qual = 'negligible'
        elif V < 0.17:
            qual = 'small'
        elif V < 0.29:
            qual = 'medium'
        else:
            qual = 'large'
    elif df == 4:
        if V < 0.05:
            qual = 'negligible'
        elif V < 0.15:
            qual = 'small'
        elif V < 0.25:
            qual = 'medium'
        else:
            qual = 'large'
    else:
        if V < 0.05:
            qual = 'negligible'
        elif V < 0.13:
            qual = 'small'
        elif V < 0.22:
            qual = 'medium'
        else:
            qual = 'large'
    return(qual)
print(judgment_CramerV(df1,res1.loc[2,'results']))
conttable1 = pd.crosstab(complete_data['Survived_cate'], complete_data['Age_above65_female'])
print(conttable1)
df2 = min(conttable1.shape[0], conttable1.shape[1]) - 1
print(df2)
crosstab2, res2 = researchpy.crosstab(complete_data['Survived_cate'], complete_data['Age_above65_female'], test='chi-square')
print(res2)
print(judgment_CramerV(df2,res2.loc[2,'results']))