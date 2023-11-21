import pandas as pd

# Load the data
data = pd.read_csv('data.csv', header=None, names=['Date', 'Value'])

# Process the data
# Example: Remove rows with missing values
data.dropna(inplace=True)

# Example: Convert date to a specific format
data['Date'] = pd.to_datetime(data['Date']).dt.strftime('%Y-%m-%d')

# Save the transformed data
data.to_csv('transformed_data.csv', index=False)
