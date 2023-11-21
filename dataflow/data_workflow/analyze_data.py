import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

def analyze_data(file_name, label):
    data = pd.read_csv(file_name)
    mean_value = data['Value'].mean()
    median_value = data['Value'].median()
    print(f"Dataset: {label}, Mean: {mean_value}, Median: {median_value}")

    plt.figure(figsize=(10, 6))
    plt.plot(data['Date'], data['Value'], label=label)
    plt.xlabel('Date')
    plt.ylabel('Rate')
    plt.title(f'{label} Over Time')
    plt.legend()
    plt.savefig(f'plot_{file_name}.png')

    with open('report.md', 'a') as file:
        file.write(f"\n## Analysis Results for {label} (Generated on {datetime.now().strftime('%Y-%m-%d %H:%M:%S')})\n")
        file.write(f"- Mean: {mean_value}\n")
        file.write(f"- Median: {median_value}\n")
        file.write(f"![{label}](plot_{file_name}.png)\n")

analyze_data('transformed_data_10_2_year_spread.csv', '10-2 Year Treasury Spread')
analyze_data('transformed_data_10_3_month_spread.csv', '10-3 Month Treasury Spread')
analyze_data('transformed_data_10_year_minus_fed_funds_rate.csv', '10 Year Treasury Minus Fed Funds Rate')
analyze_data('transformed_data_10_year_treasury.csv', '10 Year Treasury Yield')
analyze_data('transformed_data_aaa_corporate_bond_yield.csv', 'AAA Corporate Bond Yield')
analyze_data('transformed_data_baa_corporate_bond_yield.csv', 'BAA Corporate Bond Yield')

