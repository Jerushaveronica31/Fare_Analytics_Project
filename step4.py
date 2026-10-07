import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Load the dataset
df = pd.read_excel('Smart_Fare_Collection_Dataset.xlsx')

# Convert time columns and extract hour
df['Entry_Time'] = pd.to_datetime(df['Entry_Time'])
df['Entry_Hour'] = df['Entry_Time'].dt.hour

# Set visual style
sns.set_theme(style="whitegrid")
plt.figure(figsize=(12, 5))

# Chart 1: Passenger Volume by Entry Hour
plt.subplot(1, 2, 1)
sns.countplot(data=df, x='Entry_Hour', palette='viridis')
plt.title('Passenger Traffic by Entry Hour')
plt.xlabel('Hour of the Day')
plt.ylabel('Number of Passengers')

# Chart 2: Payment Status Distribution
plt.subplot(1, 2, 2)
payment_counts = df['Payment_Status'].value_counts()
plt.pie(payment_counts, labels=payment_counts.index, autopct='%1.1f%%', colors=['#4CAF50', '#F44336'])
plt.title('Payment Status Distribution')

plt.tight_layout()
plt.show()