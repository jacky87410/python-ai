import numpy as np 
import pandas as pd    
import math     
import seaborn as sns 
import matplotlib.pyplot as plt 
import statistics 
from scipy import stats 
from IPython.display import display
from IPython.display import display_html
def display_side_by_side(*args):
    html_str = ""
    for df in args:
        html_str += df.to.html()
    display_html(html_str.replace('table','table style = "display:inline"'),raw = True)
df_train = pd.read_csv("Titanic_train.csv")
df_test = pd.read_csv("Titanic_test.csv")
# %matplotlib inline
#測試 + 訓練資料集中，是否有遺失值？
#課程範例以訓練資料集來檢視，先看一下測試資料特性，再把測試資料集和訓練資料集合併，並回答下列問題。
#目的：讓大家熟悉對應這樣的問題，我們要提取怎樣的函數來進行計算。 
#Q1：觀察測試(test) 資料集和訓練(Train) 資料集的變數的差異性？
#訓練資料集比測試資料集多了Survived變數
print(df_train.info())
print(df_test.info())
#Q2：測試資料集是否有遺失值？
#有遺失值
print(df_train.isnull().sum())
#Q3：從合併資料選取一個變數，嘗試去做各種不同遺失值的處理，並透過圖形或數值來做輔助判斷，
#補值前與後的差異，你覺得以這個變數而言，試著說明每一個方法的差異。 
#補值前遺失的死亡率較高，補值後死亡率較接近T
data = df_train.append(df_test)
print(data.isnull().sum())
data["Cabin"] = data['Cabin'].apply(lambda x : str(x)[0] if not pd.isnull(x) else 'NoCabin')
sns.countplot(data["Cabin"],hue = data['Survived'])
plt.show()
print(data.groupby('Cabin', as_index=False)['Survived'].mean().sort_values(by = 'Survived', ascending = False))
