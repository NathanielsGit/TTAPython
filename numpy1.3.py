#Extract all the odd numbers from an array of 1-10
import numpy as np
array = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print(array[0:10])
print("The following are the separated arrays: ")
odd_i = []
even_i = []
for i in range(0, len(array)):
    if i % 2:
        even_i.append(array[i])
    else:
        odd_i.append(array[i])
odd = odd_i
even = even_i

# print result
print("Separated odd list: " + str(odd))
print("Separated even list: " + str(even))