import pandas as pd

# 1. Load the dataset
df = pd.read_excel('Smart_Fare_Collection_Dataset.xlsx')

# Convert time columns
df['Entry_Time'] = pd.to_datetime(df['Entry_Time'])
df['Exit_Time'] = pd.to_datetime(df['Exit_Time'])

# 2. Key Revenue Metrics
total_revenue = df['Total_Fare_INR'].sum()
avg_fare = df['Total_Fare_INR'].mean()

print("=== REVENUE METRICS ===")
print(f"Total Revenue Collected: INR {total_revenue:,.2f}")
print(f"Average Fare per Trip: INR {avg_fare:.2f}\n")

# 3. Busy Stations
print("=== TOP 5 ENTRY STATIONS ===")
print(df['Entry_Station'].value_counts().head())

print("\n=== TOP 5 EXIT STATIONS ===")
print(df['Exit_Station'].value_counts().head())

# 4. Payment Status Breakdown
print("\n=== PAYMENT STATUS BREAKDOWN ===")
print(df['Payment_Status'].value_counts())

# 5. Peak Hours Breakdown (Top 5 busiest hours)
print("\n=== TOP 5 BUSIEST HOURS ===")
df['Entry_Hour'] = df['Entry_Time'].dt.hour
print(df['Entry_Hour'].value_counts().head())