# 5. Matrix Multiplication
import numpy as np

# Define two 2x2 matrices
matrix1 = np.array([[1, 2], [3, 4]])
matrix2 = np.array([[5, 6], [7, 8]])

# Perform matrix multiplication
product_matrix = np.dot(matrix1, matrix2)

print("Matrix 1:\n", matrix1)
print("Matrix 2:\n", matrix2)
print("Product Matrix:\n", product_matrix)