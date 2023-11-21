import pandas as pd
import matplotlib.pyplot as plt

# Load the transformed data
data = pd.read_csv('transformed_data.csv')

# Basic Statistical Analysis
# Example: Calculate mean, median, etc.
mean_value = data['Value'].mean()
median_value = data['Value'].median()
print(f"Mean: {mean_value}, Median: {median_value}")

# Graph Generation
# Example: Time Series Plot
plt.figure(figsize=(10, 6))
plt.plot(data['Date'], data['Value'], label='10-Year Treasury Constant Maturity Rate')
plt.xlabel('Date')
plt.ylabel('Rate')
plt.title('10-Year Treasury Constant Maturity Rate Over Time')
plt.legend()
plt.savefig('rate_over_time.png')
plt.show()
