import numpy as np 
array1 = np.array(range(30))
#1.將上列陣列(array1)，轉成維度為(5X6)的 array，順序按列填充。(hint:order="F")
array = array1.reshape((5,6),order = "F")
print(array)
#2.呈上題的 array，找出被 6 除餘 1 的數的索引
print(np.where(array % 6 == 1))