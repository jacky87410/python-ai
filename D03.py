import numpy as np 
#1.正常的談話的聲壓為 20000 微巴斯卡，請問多少分貝?
V1 = 20000
V0 = 20
GdB = 20*np.log10(V1/V0)
print(GdB)
#2.30 分貝的聲壓會是 50 分貝的幾倍?
GdB = 30
GdB1 = 50 
v1_30 = 20*(np.power(10,GdB/20))
v2_50 = 20*(np.power(10,GdB1/20))
print(v1_30/v2_50)