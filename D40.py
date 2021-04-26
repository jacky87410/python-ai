import numpy as np 
import pandas as pd 
import seaborn as sns 
import matplotlib.pyplot as plt 
import math 
import statistics 
from scipy import stats 
from IPython.display import display
import pingouin as pg 
import researchpy
df_train = pd.read_csv("Titanic_train.csv")
print(df_train.info())
df_train["Survived_cate"] = df_train["Survived"].astype("object")
print(df_train.info())
#在鐵達尼資料集中，今天我們專注觀察變數之間的相關性，以 Titanic_train.csv 中，首先將有遺失值的數值刪除，並回答下列問題。
#Q1：透過數值法計算 Age 和 Survived 是否有相關性？
#無相關
ano = pg.anova(dv='Age', between='Survived_cate', data=df_train, detailed=True)
eta = ano.SS[0] / (ano.SS[0] + ano.SS[1])
def judgment_eta(eta):
    if eta < .01:
        qual = 'Negligible'
    elif eta < .06:
        qual = 'Small'
    elif eta < .14:
        qual = 'Medium'
    else:
        qual = 'Large'
    return(qual)
print(judgment_eta(eta))
#Q2：透過數值法計算 Sex 和 Survived 是否有相關性？
#極度高相關
contTable = pd.crosstab(df_train['Sex'], df_train['Survived_cate'])
df = min(contTable.shape[0], contTable.shape[1]) - 1
crosstab, res = researchpy.crosstab(df_train['Sex'], df_train['Survived_cate'], test='chi-square')
print(res)
print("Cramer's value is",res.loc[2,'results'])
def judgment_Cramer(df,V):
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
print(judgment_Cramer(df,res.loc[2,'results']))
#Q3：透過數值法計算 Age 和 Fare 是否有相關性？
#無線性相關
corr, _=stats.pearsonr(df_train[~df_train['Age'].isnull()]['Age'], df_train[~df_train['Age'].isnull()]['Fare'])
print(corr)
g = sns.regplot(x="Age", y="Fare", color="g",data=df_train)
plt.show()