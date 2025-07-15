### 2. Element-wise Operations on Two Arrays
import numpy as np

# Create two NumPy arrays
array1 = np.array([10, 20, 30, 40, 50])
array2 = np.array([5, 4, 3, 2, 1])

# Perform element-wise operations
sum_array = array1 + array2
difference_array = array1 - array2
product_array = array1 * array2
quotient_array = array1 / array2

print("Sum:", sum_array)
print("Difference:", difference_array)
print("Product:", product_array)
print("Quotient:", quotient_array)