import numpy as np  
import pandas as pd 
import statistics 
import math  
import matplotlib.pyplot as plt 
import seaborn as sns 
from scipy import stats 
from IPython.display import display 
from sklearn import preprocessing
df_train = pd.read_csv("Titanic_train.csv")
#在鐵達尼資料集中，透過進階補值方法 KNN，將鐵達尼號中的 Titanic_train.csv 中的 age 的遺失值進行補值。
#step1：觀察 Age 和 Pclass 和 Sex 是否有關連性?
#step2：如果有關連性，運用 KNN ，取出 Age 、 Pclass、 Sex的資料，以 Sex 與 Pclass 補 Age 遺失值。 
L = preprocessing.LabelEncoder()
df_train["Sex"] = L.fit_transform(df_train["Sex"])
sns.boxplot(x = "Pclass",y = "Age",hue = "Sex",data = df_train)
plt.show()
df = df_train[["Age","Pclass","Sex"]]
print(df.isnull().sum())
value_neighbors = 1
from sklearn.impute import KNNImputer
imputer =KNNImputer(n_neighbors= value_neighbors,weights= "uniform")
data = pd.DataFrame(imputer.fit_transform(df),columns=['Age','Pclass','Sex'])
print(data["Age"].isnull().sum())