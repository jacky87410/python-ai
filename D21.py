import matplotlib.pyplot as plt 
import numpy as np 
import pandas as pd 
#1.畫出 cos 圖檔，並儲存
x = np.arange(0,360)
y = np.cos(x*np.pi/180)
# plt.plot(x,y)
# plt.savefig("filename.png",dpi = 300 , format = "png")
#2.給定散點圖顏色
n = 1024
X = np.random.normal(0,1,n)
Y = np.random.normal(0,1,n)
T = np.arctan2(Y,X)
plt.scatter(X,Y,s = 75,c=T,alpha=.5)
plt.xlim(-1.5,1.5)
plt.ylim(-1.5,1.5)
plt.show()