import numpy as np 
name_list = ['小明','小華','小菁','小美','小張','John','Mark','Tom']
sex_list = ['boy','boy','girl','girl','boy','boy','boy','boy']
weight_list = [67.5,75.3,50.1,45.5,80.8,90.4,78.4,70.7]
rank_list = [8,1,5,4,7,6,2,3]
myopia_list = [True,True,False,False,True,True,False,False]
#1.將上列 list 依照['name', 'sex', 'weight', 'rank', 'myopia']順序擺入 array，並且資料型態順序擺入[Unicode,Unicode,float,int,boolean]
dt = np.dtype({'names':('Name', 'sex', 'weight', 'rank','Ture'), 'formats':((np.str_,4),'U4', float,int, bool)})
array = np.zeros(8,dtype= dt)
array["Name"] = name_list
array["sex"] = sex_list
array["weight"] = weight_list
array["rank"] = rank_list
array["Ture"] = myopia_list
print(array)
#2.呈上題，將 array 中體重(weight)數據集取出算出全部平均體重
#69.8375
t_weight = 0
for i in range(len(array['weight'])):
    t_weight = t_weight + array[i]['weight']
n_t_wight = t_weight/len(array['weight'])
print(n_t_wight)
#3.呈上題，進一步算出男生(sex 欄位是 boy)平均體重、女生(sex 欄位是 girl)平均體重
#男生體重：77.18333333333332   女生體重：47.8
b_weight = 0
g_weight = 0
b_sum = 0
g_sum = 0
for i in range(len(array['sex'])):
    if array[i]["sex"] == "boy":
        b_sum += 1
        b_weight = b_weight + array[i]['weight']
    else:
        g_sum += 1
        g_weight = g_weight + array[i]['weight']
n_b_weight = b_weight/b_sum
n_g_weight = g_weight/g_sum
print(n_b_weight)
print(n_g_weight)