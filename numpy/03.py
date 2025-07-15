# 3. Generate a Random Array and Find Basic Statistics
import numpy as np

# Generate a random array with 10 elements
random_array = np.random.rand(10)
print("Random Array : ",random_array)

# Calculate mean, median, and standard deviation
mean_value = np.mean(random_array)
median_value = np.median(random_array)
std_deviation = np.std(random_array)

print("Mean:", mean_value)
print("Median:", median_value)
print("Standard Deviation:", std_deviation)