import pandas as pd
import numpy as np

# ------------------------------------------
# Homework 1: Basic DataFrame Manipulations
# ------------------------------------------

# Creating the DataFrame
data = {
    'First Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [25, 30, 35, 40],
    'City': ['New York', 'San Francisco', 'Los Angeles', 'Chicago']
}
df = pd.DataFrame(data)

# 1. Rename column names using a function
df.columns = [col.lower().replace(" ", "_") for col in df.columns]  # First Name -> first_name, Age -> age

# 2. Print the first 3 rows
print("Homework 1 - First 3 rows:")
print(df.head(3))

# 3. Find the mean age
mean_age = df['age'].mean()
print("\nMean Age:", mean_age)

# 4. Select and print only the 'first_name' and 'city' columns
print("\nName and City columns:")
print(df[['first_name', 'city']])

# 5. Add a new column 'salary' with random salary values
df['salary'] = np.random.randint(4000, 10000, size=len(df))
print("\nDataFrame with Salary column added:")
print(df)

# 6. Display summary statistics of the DataFrame
print("\nSummary statistics:")
print(df.describe())

# ------------------------------------------
# Homework 2: Sales and Expenses DataFrame
# ------------------------------------------

sales_data = {
    'Month': ['Jan', 'Feb', 'Mar', 'Apr'],
    'Sales': [5000, 6000, 7500, 8000],
    'Expenses': [3000, 3500, 4000, 4500]
}
sales_and_expenses = pd.DataFrame(sales_data)

# 1. Max sales and expenses
print("\nHomework 2 - Maximum Sales:", sales_and_expenses['Sales'].max())
print("Maximum Expenses:", sales_and_expenses['Expenses'].max())

# 2. Min sales and expenses
print("Minimum Sales:", sales_and_expenses['Sales'].min())
print("Minimum Expenses:", sales_and_expenses['Expenses'].min())

# 3. Average sales and expenses
print("Average Sales:", sales_and_expenses['Sales'].mean())
print("Average Expenses:", sales_and_expenses['Expenses'].mean())

# ------------------------------------------
# Homework 3: Monthly Expenses DataFrame
# ------------------------------------------

expense_data = {
    'Category': ['Rent', 'Utilities', 'Groceries', 'Entertainment'],
    'January': [1200, 200, 300, 150],
    'February': [1300, 220, 320, 160],
    'March': [1400, 240, 330, 170],
    'April': [1500, 250, 350, 180]
}
expenses = pd.DataFrame(expense_data)

# Set 'Category' as the index
expenses = expenses.set_index('Category')

# 1. Max expense per category
print("\nHomework 3 - Maximum expense per category:")
print(expenses.max(axis=1))

# 2. Min expense per category
print("\nMinimum expense per category:")
print(expenses.min(axis=1))

# 3. Average expense per category
print("\nAverage expense per category:")
print(expenses.mean(axis=1))

# Homework 1:
# - Create a DataFrame and rename columns
# - Show first 3 rows and mean age
# - Print selected columns
# - Add random salary values
# - Show summary statistics (mean, std, etc.)

# Homework 2:
# - Create monthly sales and expenses table
# - Calculate max, min, and average values

# Homework 3:
# - Create category-based monthly expenses
# - Use .set_index() to make Category the index
# - Show max, min, and mean for each row (axis=1)
