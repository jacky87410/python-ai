import numpy as np 
a = np.arange(21)
print(a)
for i in range(len(a)):
    if a[i]%2 == 0:
        print(a[i],end=" ")
print(" ")        
for i in range(len(a)):
    if a[i]%3 == 0 and a[i] != 0:
        print(a[i],end=" ")
print(" ")

