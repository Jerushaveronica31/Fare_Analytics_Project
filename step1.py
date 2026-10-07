import pandas as pd

# 1. Load the Excel file
df = pd.read_excel('Smart_Fare_Collection_Dataset.xlsx')

# 2. Inspect the first 5 rows
print("--- First 5 Rows ---")
print(df.head())

# 3. View dataset details and data types
print("\n--- Dataset Information ---")
print(df.info())

# 4. Total rows and columns
print("\n--- Shape (Rows, Columns) ---")
print(df.shape)