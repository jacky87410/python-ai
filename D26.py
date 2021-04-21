import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns 
from bokeh.plotting import figure,output_file,show
from bokeh.sampledata.stocks import AAPL
import bokeh.io 
from bokeh.resources import INLINE
bokeh.io.reset_output()
bokeh.io.output_notebook(INLINE)
#作業: 
#1.建立簡單的水果資料集
output_file("fruit.html")
fruits = ['Apples', 'Pears', 'Nectarines', 'Plums', 'Grapes', 'Strawberries']
counts = [5, 3, 4, 2, 4, 6]
p = figure(plot_height=300,x_range=fruits, title="Fruit Counts",toolbar_location=None, tools="")
p.vbar(x=fruits, top=counts, width=0.9)
p.y_range.start = 0
show(p)
#2. 利用 Source 建立字典, 再用figure 輸出 BAR 圖
# source = ColumnDataSource(data=dict(fruits=fruits, counts=counts, color=Spectral6))
output_file("fruit2.html")
sorted_fruits = sorted(fruits, key=lambda x: counts[fruits.index(x)])
p = figure(plot_height=300,x_range=sorted_fruits, title="Fruit Counts",toolbar_location=None, tools="")
p.vbar(x=fruits, top=counts, width=0.9)
p.y_range.start = 0
show(p)
