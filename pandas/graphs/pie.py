import pandas as pd
import matplotlib.pyplot as plt
data = {'Date': ['10–01–16', '10–02–16', '10–03–16', '10–04–16', '10–05–16', '10–06–16', '10–07–16'],
        'Open': [770.25, 776.030029, 774.25, 776.030029, 779.3541998, 776.306698, 779.659973],
        'High': [776.075902, 778.730022, 776.065702, 771.710022, 782.073407, 782.46398, 782.32],
        'Low': [769.5, 780.890015, 766.5, 772.890015, 775.650024, 775.539978, 765.23],
        'Close': [782.659998, 776.429993, 772.549798, 776.429993, 776.469971, 776.859985, 769.23]}

df = pd.DataFrame(data)
print(df)


#7
df['Open'].value_counts().plot(kind='pie', autopct='%1.1f%%', colors=['red','cyan', 'blue', 'green', 'orange', 'purple','black'])
plt.title('Pie Chart - Open Values')
plt.show()