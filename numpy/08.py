import numpy as np

arr = np.array([3, 6, 9])
arr1=np.array([7,8,6])
x = np.lcm(arr,arr1)
y = np.gcd(arr,arr1)
print(f"LCM = {x}\nGCD = {y}")