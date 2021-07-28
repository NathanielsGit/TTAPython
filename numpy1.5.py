#Convert a 1D array to a 2D array with 2 rows
import numpy as np
array = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
newArray = array.reshape(2, 6)
print(newArray)