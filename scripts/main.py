import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the Fitbit dataset (assuming it's a CSV file in 'data/')
data_path = "data/fitbit_data.csv"  # Replace with actual filename
df = pd.read_csv(data_path)

# Simple data exploration
print(df.head())
print(df.describe())

# Visualize the distribution of steps over time (or any other feature)
plt.figure(figsize=(10, 6))
sns.histplot(df['Steps'], bins=30, kde=True)
plt.title('Distribution of Steps')
plt.xlabel('Steps')
plt.ylabel('Frequency')
plt.show()

# (Additional code for data processing, model training, etc. can go here)
