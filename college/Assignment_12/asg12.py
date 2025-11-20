import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
data = pd.read_csv('sample.csv')
regions = list(np.unique(data['Region']))
# # print(data.columns)
sales = []
for r in regions:
    data1 = data.loc[data['Region']==r,['Sales']]
    sales.append(data1['Sales'].sum())
region_wise_sales = {'Regions': regions, 'Total Sales': sales}
region_sale = pd.DataFrame(region_wise_sales)
# # print(region_sale)
figure, (axis1,axis2) = plt.subplots(1, 2)
# print(axis)
axis1.bar(region_sale["Regions"], region_sale["Total Sales"],)
axis2.pie(region_sale["Total Sales"],labels=region_sale["Regions"])
# # axis2.plt.show()
plt.show()