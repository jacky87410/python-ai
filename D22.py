import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt
from sklearn import datasets 
#條型圖：Bar Plots
    #長條圖主要用來呈現兩個維度的資料，一個為X軸另一個則為Y軸(當然這邊指的是二維的狀況，較為常見)
    #主要用來呈現兩個維度的資料
    #問題：嘗試通過添加紅色條形標籤重現右側的圖形。
n = 12
X = np.arange(n)
Y1 = (1-X/float(n)) * np.random.uniform(0.5,1.0,n)
Y2 = (1-X/float(n)) * np.random.uniform(0.5,1.0,n)
plt.bar(X, +Y1,facecolor = "#9999ff",edgecolor = "white")
plt.bar(X, -Y2,facecolor = "red",edgecolor = "white")
for x,y in zip(X,Y1):
    plt.text(x+0.4,y+0.5,"%.2f" % y,ha = "center",va = "bottom")
plt.ylim(-1.25,+1.25)
plt.show()
#軸圖進階
    #但是可以將圖放置在圖中的任何位置。因此，如果要在較大的圖中放置較小的圖，則可以使用軸。
    #特別提醒：tick 刻度線定位器
    #問題：使用 tick
plt.axes([0.1,0.1,.5,.5])
plt.xticks([]),plt.yticks([])
plt.text(0.1,0.1,"axes([0.1,0.1,.5,.5])",ha = "left",va = "center",size = 16,alpha = .5)
plt.axes([0.2,0.2,.4,.4])
plt.xticks([]),plt.yticks([])
plt.text(0.2,0.2,"axes([0.2,0.2,.4,.4])",ha = "left",va = "center",size = 14,alpha = .5)
plt.axes([0.3,0.3,.3,.3])
plt.xticks([]),plt.yticks([])
plt.text(0.3,0.3,"axes([0.3,0.3,.3,.3])",ha = "left",va = "center",size = 12,alpha = .5)
plt.axes([0.4,0.4,.2,.2])
plt.xticks([]),plt.yticks([])
plt.text(0.4,0.4,"axes([0.4,0.4,.2,.2])",ha = "left",va = "center",size = 10,alpha = .5)
plt.axes([0.5,0.5,.1,.1])
plt.xticks([]),plt.yticks([])
plt.text(0.5,0.5,"axes([0.5,0.5,.1,.1])",ha = "left",va = "center",size = 8,alpha = .5)
plt.show()