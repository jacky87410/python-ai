import numpy as np 
#1.生成一個等差數列，首數為 0，尾數為 20，公差為 1 的數列。
a = np.arange(21) 
print(a)
#2.呈上題，將以上數列取出偶數。
for i in range(len(a)): 
    if a[i]%2 == 0:
        print(a[i],end=" ")
print(" ")
#3.呈 1 題，將數列取出 3 的倍數。
for i in range(len(a)):
    if a[i]%3 == 0 and a[i] != 0:
        print(a[i],end=" ")
print(" ")

