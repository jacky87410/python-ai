import pandas as  pd 
#讀取 STOCK_DAY_0050_202009.csv 串聯 STOCK_DAY_0050_202010.csv，並且找出 open 小於 close 的資料
data_09 = pd.read_csv("STOCK_DAY_0050_202009.csv")
data_10 = pd.read_csv("STOCK_DAY_0050_202010.csv")
print(data_09.head())
print(data_10.head())
new_data = pd.concat([data_09,data_10],axis=0)
print(new_data)
print(new_data.loc[new_data.open<new_data.close])