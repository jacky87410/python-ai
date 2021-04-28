import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns 
import math  
import statistics 
from scipy import stats 
from IPython import display
from sklearn.preprocessing import LabelEncoder
a = pd.read_csv("A_lvr_land_A.csv")
b = pd.read_csv("B_lvr_land_A.csv")
e = pd.read_csv("E_lvr_land_A.csv")
f = pd.read_csv("F_lvr_land_A.csv")
print(a.head())
a = a.drop(0)
b = b.drop(0)
e = e.drop(0)
f = f.drop(0)
a["city"] = "Taipei"
b['city'] = 'Taichung'
e['city'] = 'Kaohsiung'
f['city'] = 'New_Taipei'
four_city = pd.concat([a,b,e,f],axis = 0)
print(four_city.tail())
columns_mapping = {'鄉鎮市區':'towns',
'交易標的':'transaction_sign',
'土地區段位置建物區段門牌':'house_number',
'土地移轉總面積平方公尺':'land_area_square_meter', 
'都市土地使用分區':'use_zoning', 
'非都市土地使用分區':'land_use_district',
'非都市土地使用編定':'land_use',
'交易年月日':'tx_dt', 
 '交易筆棟數':'transaction_pen_number', 
 '移轉層次':'shifting_level', 
 '總樓層數':'total_floor_number', 
 '建物型態':'building_state', 
 '主要用途':'main_use', 
 '主要建材':'main_materials',
 '建築完成年月':'complete_date', 
 '建物移轉總面積平方公尺':'building_area_square_meter', 
 '建物現況格局-房':'room_number', 
 '建物現況格局-廳':'hall_number', 
 '建物現況格局-衛':'health_number', 
'建物現況格局-隔間':'compartmented_number', 
 '有無管理組織':'manages', 
 '總價元':'total_price', 
 '單價元平方公尺':'unit_price', 
 '車位類別':'berth_category', 
 '車位移轉總面積(平方公尺)':'berth_area_square_meter',
'車位總價元':'berth_price', 
 '備註':'note', 
 '編號':'serial_number', 
 '主建物面積':'main_building_area', 
 '附屬建物面積':'auxiliary_building_area', 
 '陽台面積':'balcony_area', 
 '電梯':'elevator'
                  }
analysis_columns = ['city','towns','main_use','use_zoning','total_price','building_area_square_meter',
                                     'main_building_area',
                                     'tx_dt','unit_price','room_number','hall_number','health_number']
columns_type = {'total_price': 'int','unit_price':'float','building_area_square_meter':'float',
                                      'main_building_area': 'float',
                                      'room_number': 'int','hall_number': 'int','health_number': 'int'}
four_city = four_city.rename(columns = columns_mapping)
print(four_city.head())
home = four_city[(four_city['main_use']=='住家用') & (four_city['use_zoning']=='住')]
print(len(home))
home = home.dropna(axis=0,how='any',subset=analysis_columns)
print(len(home))
print(type(home['total_price'][1]))
home = home.astype(columns_type)
print(type(home['total_price'][1]))
def year(date):
    date[:2]=='109'
def year(date):
    y = date[:3]
    if y =='109':
        return "109"
home['tx_dt_year'] = home['tx_dt'].apply(year)
print(len(home))
buy109 = home[home['tx_dt_year']=='109']
print(len(buy109))
want = buy109[(buy109['room_number']>0) & (buy109['room_number']<=5) & 
             (buy109['hall_number']>0) & (buy109['hall_number']<=2)]
print(len(want))
want = want.reset_index()
want['building_area_square_feet'] = want['building_area_square_meter'].apply(lambda a : a * 0.3025)
want['main_building_area_square_feet'] = want['main_building_area'].apply(lambda a : a * 0.3025)
want['unit_price_square_feet'] = want['unit_price'].apply(lambda a : a/0.3025)
print(want.describe())
want.drop(want[want['total_price']==0].index, inplace=True)
want.drop(want[want['unit_price']==0].index, inplace=True)
want.drop(want[want['main_building_area']==0].index, inplace=True)
print(len(want))
print(want.describe())
analysis_columns = ['city','towns','main_use','use_zoning','total_price','building_area_square_meter',
                                     'main_building_area',
                                     'tx_dt','unit_price','room_number','hall_number','health_number',
                    'building_area_square_feet','main_building_area_square_feet','unit_price_square_feet','tx_dt_year']

want1 = want.loc[:,analysis_columns] 
print(want1.head(2))
tpe = want1[want1['city']=='Taipei']


result1 = stats.pearsonr(tpe['room_number'],tpe['total_price'])
result2 = stats.pearsonr(tpe['hall_number'],tpe['total_price'])
result3 = stats.pearsonr(tpe['health_number'],tpe['total_price'])
result4 = stats.pearsonr(tpe['building_area_square_feet'],tpe['total_price'])
result5 = stats.pearsonr(tpe['main_building_area_square_feet'],tpe['total_price'])
print("與總價相關性：\n房:",f"{result1}","\n廳:",f"{result2}","\n衛:",f"{result3}",
      "\n建物移轉總面積坪:",f"{result4}","\n主建物面積坪:",f"{result5}")
result6 = stats.pearsonr(tpe['room_number'],tpe['unit_price_square_feet'])
result7 = stats.pearsonr(tpe['hall_number'],tpe['unit_price_square_feet'])
result8 = stats.pearsonr(tpe['health_number'],tpe['unit_price_square_feet'])
result9 = stats.pearsonr(tpe['building_area_square_feet'],tpe['unit_price_square_feet'])
result10 = stats.pearsonr(tpe['main_building_area_square_feet'],tpe['unit_price_square_feet'])
print("與單價元坪相關性：\n房:",f"{result6}","\n廳:",f"{result7}","\n衛:",f"{result8}",
      "\n建物移轉總面積坪:",f"{result9}","\n主建物面積坪:",f"{result10}")
sns.boxplot(x='city',y='unit_price_square_feet',data=want1)
plt.show()
sns.boxplot(x='room_number',y='total_price',data=tpe)
plt.show()
le = LabelEncoder()
tpe['towns_label'] = le.fit_transform(tpe['towns'])
sns.boxplot(x='towns_label',y='unit_price_square_feet',data=tpe)
plt.show()
print(le.inverse_transform([8]))
