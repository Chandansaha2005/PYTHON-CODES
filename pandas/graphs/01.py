import pandas as pd
data = {
    'Roll': [100, 102, 103, 104],
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Total Marks': [85, 92, 78, 88],
    'Class': ['10th', '10th', '10th', '12th']
}
df = pd.DataFrame(data)
df_sorted = df.sort_values(by=['Name'], ascending=True)
print(df_sorted)