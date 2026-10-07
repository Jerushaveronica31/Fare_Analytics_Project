import pandas as pd

# 1. Load the dataset
df = pd.read_excel('Smart_Fare_Collection_Dataset.xlsx')

# 2. Check for missing values
print("--- Missing Values Count ---")
print(df.isnull().sum())

# 3. Convert time strings to datetime format
df['Entry_Time'] = pd.to_datetime(df['Entry_Time'])
df['Exit_Time'] = pd.to_datetime(df['Exit_Time'])

# 4. Feature Engineering: Calculate travel duration in minutes
df['Calculated_Duration_Min'] = (df['Exit_Time'] - df['Entry_Time']).dt.total_seconds() / 60

# 5. Extract Entry Hour for peak hour analysis
df['Entry_Hour'] = df['Entry_Time'].dt.hour

print("\n--- Processed Dataset Preview ---")
print(df[['Entry_Time', 'Exit_Time', 'Calculated_Duration_Min', 'Entry_Hour']].head())