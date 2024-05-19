# W:\Perso\backup\IT stuff\Cours de programmation\Python\PANDAS\Video\The Ultimate Pandas Bootcamp Advanced Python Data Analysis\[TutsNode.com] - The Ultimate Pandas Bootcamp Advanced Python Data Analysis\1. Introduction


import pandas as pd
import numpy as np

# print numpy version
print(pd.__version__)

# n-dimensional array: a collection of elements
a_py = [10, 20, 40, 23, 123, 1233]
print(type(a_py))

b_np = np.array([10, 20, 40, 23, 123, 1233])
print(type(b_np))

"""
Handling numpy object is much quicker than with traditiona list
this is due to numpy memory for an object beeing contigous while a list
contains a list of pointers on memory cells. Therefore, numpy has much better
performance and smaller memory footprint. This is a 
trade off: numpy arrays contain only one data type
"""

# Let's multiply all the numbers by 10
# with a traditional list
arr = []
for i in a_py:
    arr.append(i * 10)
print(arr)

# with map(lambda)
print(list(map(lambda i: i * 10, a_py)))

# with a list comprehension
print([i * 10 for i in a_py])

# in numpy
print(b_np * 10)

# trade off: numpy arrays contain only one data type
c_np = np.array([1, 2, 3])
print(type(c_np.dtype))

