import numpy as np

arr1 = np.array([[1, 2], [3, 4]])
arr2 = np.array([[5, 6], [7, 8]])
arr3 = np.array([[15, 66], [27, 88]])

arr = np.concatenate((arr1, arr2, arr3), axis=1)

print(arr)