import numpy as np

# Step 1: Generate a synthetic dataset with 3 features
np.random.seed(5)
data = np.random.rand(5, 3)  # 100 samples, 3 features

print("Data = \n",data)
# Step 2: Standardize the data (mean = 0, variance = 1)
mean = np.mean(data, axis=0)
standardized_data = data - mean
print("mean = \n",mean)
print("Standardized data = ",standardized_data)
# Step 3: Calculate the covariance matrix
cov_matrix = np.cov(standardized_data, rowvar=False)
print("Co-varient = ",cov_matrix)
# Step 4: Perform eigen decomposition on the covariance matrix
eigenvalues, eigenvectors = np.linalg.eig(cov_matrix)

# Step 5: Sort eigenvalues and their corresponding eigenvectors in descending order
sorted_indices = np.argsort(eigenvalues)[::-1]
sorted_eigenvalues = eigenvalues[sorted_indices]
sorted_eigenvectors = eigenvectors[:, sorted_indices]

# Step 6: Select the top k eigenvectors (principal components)
k = 2  # Reduce to 2 dimensions
principal_components = sorted_eigenvectors[:, :k]

# Step 7: Transform the data to the new subspace
reduced_data = np.dot(standardized_data, principal_components)

# Output the results
print("Original Data Shape:", data.shape)
print("Reduced Data Shape:", reduced_data.shape)
print("Principal Components:\n", principal_components)
print("Reduced Data:\n", reduced_data[:5])  # Display first 5 samples of reduced data
