import numpy as np
arr3 = np.array([[[3,6],[8,4]],[[7,1],[2,5]]])
print(arr3)

# search
fi = np.where(arr3 == 2)
print(fi)

# sort
sim = np.sort(arr3)
print(sim)