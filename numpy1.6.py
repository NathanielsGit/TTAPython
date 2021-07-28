#Create two arrays a and b, stack these two arrays vertically use the np. np.sum to calculate totals
import numpy as np
array1 = ([1, 3, 5, 7, 9], [11, 13, 15, 17, 19])
array2 = ([0, 2, 4, 6, 8], [10, 12, 14, 16, 18])
print(array1)
print(array2)

print("here is your Vertical array")

vstack = np.vstack((array1,array2))
print(vstack)
