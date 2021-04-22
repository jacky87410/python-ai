import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns 
from mpl_toolkits.basemap import Basemap
#1.  更改 Projection 的設定繪製出地球儀圖形
#當 "projection" 參數為“ortho"時，所得圖位地球儀截面
fig = plt.figure(figsize=(8,6),edgecolor="w")
m = Basemap(projection ='ortho',lat_0 = 0,lon_0 = 0)
m.bluemarble()
plt.show()
#當 "projection" 參數為“Mill"時，所得平展位面
fig = plt.figure(figsize=(8,6),edgecolor="w")
m = Basemap(width=12000000,height=9000000,projection='lcc',resolution=None,lat_1=45.,lat_2=55,lat_0=50,lon_0=-107.)
m.bluemarble()
plt.show()
#2.  查看 resolution / 經緯度座標的繪圖精細度 
fig = plt.figure(figsize = (8,6),edgecolor = 'w')
m = Basemap(projection='mill',llcrnrlat=-90,urcrnrlat=90,llcrnrlon=-180,urcrnrlon=180)
m.drawcoastlines()
m.drawcountries()
m.drawstates(color = 'b')
m.drawcounties(color = 'darkred')
plt.title("Basemap Tutorial")
plt.show()
