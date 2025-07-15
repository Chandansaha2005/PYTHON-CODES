import numpy as np

def myadd(x, y,z):
  return x+y+z

myadd = np.frompyfunc(myadd, 3, 1)

print(myadd([1, 2, 3, 4], [5, 6, 7, 8],[0,1,2,3]))