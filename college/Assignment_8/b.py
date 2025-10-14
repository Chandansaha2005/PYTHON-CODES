import numpy as np
m = int(input("\nEnter number of rows (m): "))
n = int(input("Enter number of columns (n): "))

# Create matrix A with user input
A = []
print("\nEnter elements of matrix A:")
for i in range(m):
    row = list(map(int, input(f"Row {i+1}: ").split()))
    A.append(row)

A = np.array(A)

# Create matrix B with random integers between 1 and 20
B = np.random.randint(1, 21, size=(n, 1))

# Matrix multiplication: C = A × B
C = np.dot(A, B)

print("\nMatrix A:")
print(A)
print("\nMatrix B:")
print(B)
print("\nMatrix C = A × B:")
print(C)