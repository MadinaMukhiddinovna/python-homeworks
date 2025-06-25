
import pandas as pd

# Load the sales data
sales_df = pd.read_csv('C:\Users\user\Downloads\sales_data.csv')

# 1. Group by Category and calculate:
category_stats = sales_df.groupby('Category').agg({
    'Quantity': ['sum', 'max'],        # Total and max quantity
    'Price': 'mean'                    # Average price
}).reset_index()
category_stats.columns = ['Category', 'Total_Quantity', 'Max_Quantity', 'Average_Price']

# 2. Top-selling product in each category (based on total quantity)
top_products = sales_df.groupby(['Category', 'Product'])['Quantity'].sum().reset_index()
top_products = top_products.sort_values(['Category', 'Quantity'], ascending=[True, False])
top_selling_by_category = top_products.groupby('Category').first().reset_index()

# 3. Date with highest total sales (quantity * price)
sales_df['Total_Sale'] = sales_df['Quantity'] * sales_df['Price']
daily_sales = sales_df.groupby('Date')['Total_Sale'].sum().reset_index()
highest_sales_date = daily_sales.sort_values('Total_Sale', ascending=False).head(1)



# Load the customer orders data
orders_df = pd.read_csv('C:\Users\user\Downloads\customer_orders.csv')

# 1. Group by CustomerID and filter customers with 20+ orders
orders_per_customer = orders_df.groupby('CustomerID')['OrderID'].count().reset_index(name='Order_Count')
active_customers = orders_per_customer[orders_per_customer['Order_Count'] >= 20]

# 2. Customers who ordered products with average price > $120
avg_price_per_customer = orders_df.groupby('CustomerID')['Price'].mean().reset_index()
high_spenders = avg_price_per_customer[avg_price_per_customer['Price'] > 120]

# 3. Total quantity and price for each product, filter quantity < 5
product_summary = orders_df.groupby('Product').agg({
    'Quantity': 'sum',
    'Price': 'sum'
}).reset_index()
filtered_products = product_summary[product_summary['Quantity'] >= 5]


import pandas as pd
import sqlite3

# Connect to SQLite database and read population table
conn = sqlite3.connect('C:\Users\user\Downloads\population.db')
population_df = pd.read_sql_query("SELECT * FROM population", conn)
conn.close()

# Load salary bands from Excel
bands_df = pd.read_excel("C:\Users\user\Downloads\population_salary_analysis (1).xlsx")

# Assume bands_df has columns: 'Band', 'Min_Salary', 'Max_Salary'

# Add Salary Band to each person in population
def assign_salary_band(salary):
    for _, row in bands_df.iterrows():
        if row['Min_Salary'] <= salary <= row['Max_Salary']:
            return row['Band']
    return 'Unknown'

population_df['Salary_Band'] = population_df['Salary'].apply(assign_salary_band)

# 1. Overall stats per Salary Band
overall = population_df.groupby('Salary_Band').agg(
    Population_Count=('Salary', 'count'),
    Avg_Salary=('Salary', 'mean'),
    Median_Salary=('Salary', 'median')
).reset_index()

# Calculate percentage of population per band
total_population = population_df.shape[0]
overall['Population_Percent'] = (overall['Population_Count'] / total_population) * 100

# 2. Same stats per State and Salary Band
state_band = population_df.groupby(['State', 'Salary_Band']).agg(
    Population_Count=('Salary', 'count'),
    Avg_Salary=('Salary', 'mean'),
    Median_Salary=('Salary', 'median')
).reset_index()

state_total = population_df.groupby('State')['Salary'].count().reset_index(name='Total_Pop')
state_band = pd.merge(state_band, state_total, on='State')
state_band['Population_Percent'] = (state_band['Population_Count'] / state_band['Total_Pop']) * 100
state_band = state_band.drop(columns='Total_Pop')

