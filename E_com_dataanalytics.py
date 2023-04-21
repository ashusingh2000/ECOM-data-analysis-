import pandas as pd
import matplotlib.pyplot as plt


data = pd.read_csv('sales_data.csv')




# Check for missing values
print(data.isnull().sum())

# Remove duplicates
data.drop_duplicates(inplace=True)

# Convert data types
data['date'] = pd.to_datetime(data['date'])

#Analyzing the Data


sales_by_category = data.groupby('category')['revenue'].sum().reset_index()
print(sales_by_category)



plt.bar(sales_by_category['category'], sales_by_category['revenue'])
plt.xlabel('Product Category')
plt.ylabel('Sales Revenue')
plt.title('Total Sales Revenue by Product Category')
plt.show()
