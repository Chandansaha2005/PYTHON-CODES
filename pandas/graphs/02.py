import pandas as pd
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [24, 22, 23, 25],
    'Rating': [4.5, 4.0, 4.7, 4.8]
}
df = pd.DataFrame(data)
sum_cols = df.sum(numeric_only=True)
print("Sum of Columns:\n", sum_cols)
avg_age = df['Age'].mean()
avg_rating = df['Rating'].mean()
print("Average Age:", avg_age)
print("Average Rating:", avg_rating)
std_dev = df.describe()
print("Standard Deviation:", std_dev)
desc = df.describe()
print("Description:", desc)