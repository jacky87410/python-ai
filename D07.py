import numpy as np 
array1 = np.array([[10, 8], [3, 5]])
#1. 運用上列array計算反矩陣，乘上原矩陣，並觀察是否為單位矩陣?
# 是
new_array = np.linalg.inv(array1)
print(np.matmul(array1,new_array))
#2. 運用上列array計算特徵值、特徵向量?
x,y = np.linalg.eig(array1)
print(x)
print(y)
#3. 運用上列array計算SVD?
U,sigma,VT = np.linalg.svd(array1)
print(U)
print(sigma)
print(VT)