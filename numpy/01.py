# The code snippet is demonstrating how to create and manipulate a NumPy array in Python. Here's a
# breakdown of what each part of the code does:
# 1. Create and Manipulate a NumPy Array
import numpy as np
# Create a NumPy array
# `array = np.array([1, 2, 3, 4, 5])` is creating a NumPy array with elements `[1, 2, 3, 4, 5]` and
# assigning it to the variable `array`.
array = np.array([1, 2, 3, 4, 5])
array_plus_five = array + 5
array_times_two = array * 2
print("Original Array:", array)
print("Array after adding 5:", array_plus_five)
print("Array after multiplying by 2:", array_times_two)