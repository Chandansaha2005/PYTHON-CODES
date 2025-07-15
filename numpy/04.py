### 4. Reshape a NumPy Array
import numpy as np

# Create a one-dimensional NumPy array
array = np.array([1, 2, 3, 4, 5, 6])

# Reshape the array into a 2x3 matrix
reshaped_array = array.reshape(2, 3)

print("Original Array:", array)
print("Reshaped Array:\n", reshaped_array)