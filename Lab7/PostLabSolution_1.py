import pandas as pd
import matplotlib.pyplot as plt
import os

# Load the data
csv_path = os.path.join(os.path.dirname(__file__), 'breadprice.csv')
df = pd.read_csv(csv_path)

# Clean the data: Convert all columns except 'Year' to numeric, coerce errors to NaN
for col in df.columns[1:]:
    df[col] = pd.to_numeric(df[col], errors='coerce')

# Compute the average price per year, ignoring NaN values
# (axis=1 means row-wise, i.e., across months)
df['Average'] = df.iloc[:, 1:].mean(axis=1, skipna=True)

# Plot the average price per year
plt.figure(figsize=(10, 6))
plt.plot(df['Year'], df['Average'], marker='o', linestyle='-')
plt.title('Average Bread Price per Year')
plt.xlabel('Year')
plt.ylabel('Average Price (USD)')
plt.grid(True)
plt.tight_layout()
plt.show() 