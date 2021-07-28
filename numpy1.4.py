#Replace all the odd numbers in an array of 1-10 with the value -1
import numpy as np
array1 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print(array1[0:10])
print("The following is the updated list: ")

odd_values = (array1 % 2 == 1)
array1[odd_values] = -1

print (array1)