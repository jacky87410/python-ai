import pandas as pd 
#將以下問卷資料的職業(Profession) 欄位缺失值填入字串 'others'，更進一步將字串做編碼。 此時用什麼方式做編碼比較適合？為什麼？
#使用LabelEncoder較適合，因為資料是有序離散的值
q_df = pd.DataFrame([['male', 'teacher'], ['male', 'engineer'], ['female', None], ['female', 'engineer']],columns=['Sex','Profession'])
print(q_df)
q_df["Profession"][2] = "others"
print(q_df)
from sklearn.preprocessing import LabelEncoder
labelencoder = LabelEncoder()
q_df["Sex"] =labelencoder.fit_transform(q_df["Sex"])
q_df["Profession"] =labelencoder.fit_transform(q_df["Profession"])
print(q_df)