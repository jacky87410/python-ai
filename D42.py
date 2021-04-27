import numpy as np 
import pandas as pd 
import math 
import statistics 
import seaborn as sns 
import matplotlib.pyplot as plt 
from scipy import stats
from IPython.display import display
import sklearn 
from sklearn.feature_selection import VarianceThreshold
from sklearn import preprocessing
from sklearn.datasets import make_friedman1
from sklearn.feature_selection import RFE
from sklearn.svm import SVC
df_train = pd.read_csv("Titanic_train.csv")
print(df_train.info())
df_train['Survived_cate']=df_train['Survived']
df_train['Survived_cate']=df_train['Survived_cate'].astype('object')
print(df_train.info())
complete_data=df_train.dropna()
complete_data=complete_data.drop(['Name','Ticket','PassengerId'], axis=1)
display(complete_data.head(5))
print(complete_data.shape)
num_features = []
for dtype, feature in zip(complete_data.dtypes, complete_data.columns):
    if dtype == 'float64' or dtype == 'int64':
        num_features.append(feature)
print(f'{len(num_features)} Numeric Features : {num_features}\n')
cat_features = []
for dtype, feature in zip(complete_data.dtypes, complete_data.columns):
    if dtype == 'object':
        cat_features.append(feature)
print(f'{len(cat_features)} category Features : {cat_features}\n')
x=complete_data[['Pclass', 'Age', 'SibSp', 'Parch', 'Fare','Sex', 'Embarked']]
y=complete_data['Survived']
display(x.head(5))
display(y.head(5))
#在鐵達尼資料集中，以 Titanic_train.csv 中，首先將有遺失值的數值刪除，試著將課堂中所學的方法應用上去。
#Q1：目標變數為 Survived，以 Pclass, Age, SibSp, Parch, Fare,Sex, Embarked 為特徵，試著用今天教授的包裝法，搭配課程所教的 SVC，試著排出其餘特徵的重要性。
sex_mapping = {"male":1,"female":0}
complete_data['Sex1'] = complete_data['Sex'].map(sex_mapping)
embarked_mapping = {'C':0,"Q":1,"S":2}
complete_data['Embarked1'] = complete_data['Embarked'].map(embarked_mapping)
x = complete_data[['Pclass', 'Age', 'SibSp', 'Parch', 'Fare','Sex1', 'Embarked1']]
y = complete_data["Survived"]
estimator = SVC(kernel = "linear")
selector = RFE(estimator,n_features_to_select = 2,step =1) 
selector = selector.fit(x,y)
print(selector.support_)
ranking = selector.ranking_
print(ranking)
ref_feature = x.loc[:,selector.support_].columns.tolist()
print(ref_feature)