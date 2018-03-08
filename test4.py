import numpy as np

x = np.arange(18).reshape(6,3)
print(x)

y = np.array_split(x, 3)
y = np.delete(y, 1, axis=0).reshape(-1,3)
print(y)

print(x)