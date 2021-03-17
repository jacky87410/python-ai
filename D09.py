import pandas as pd 
#讀取資料夾中 boston.csv 讀取其欄位 CHAS、NOX、RM，輸出成 .xlsx 檔案
boston_data = pd.read_csv("boston.csv",usecols=["CHAS","NOX","RM"])
print(boston_data.head())
boston_data.to_excel('new_boston.xlsx')
a = pd.read_excel("new_boston.xlsx")
print(a)