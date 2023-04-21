import pandas as pd

# Create a DataFrame
data = pd.DataFrame({
    'date': ['2022-01-01', '2022-01-02', '2022-01-03'],
    'customer_id': [1001, 1002, 1003],
    'category': ['clothing', 'electronics', 'home goods'],
    'product': ['shirt', 'phone', 'pillow'],
    'quantity': [2, 1, 3],
    'price': [25, 500, 10],
    'revenue': [50, 500, 30]
})

# Save the DataFrame as a CSV file
data.to_csv('sales_data.csv', index=False)
