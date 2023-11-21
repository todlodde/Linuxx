import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import pearsonr
from datetime import datetime

# Function to load and preprocess data
def load_data(filename):
    data = pd.read_csv(filename, parse_dates=['Date'], index_col='Date')
    return data

# Load datasets
data_10_year = load_data('transformed_data_10_year_treasury.csv')
data_10_2_year = load_data('transformed_data_10_2_year_spread.csv')
data_10_3_month = load_data('transformed_data_10_3_month_spread.csv')
data_baa_bond_yield = load_data('transformed_data_baa_corporate_bond_yield.csv')
data_10_year_minus_ffr = load_data('transformed_data_10_year_minus_fed_funds_rate.csv')
data_aaa_bond_yield = load_data('transformed_data_aaa_corporate_bond_yield.csv')


# Function for Yield Curve Analysis
def yield_curve_analysis():
    plt.figure(figsize=(12, 6))
    plt.plot(data_10_year, label='10-Year Treasury')
    plt.plot(data_10_2_year, label='10-2 Year Spread')
    plt.plot(data_10_3_month, label='10-3 Month Spread')
    plt.title('Yield Curve Analysis Over Time')
    plt.xlabel('Date')
    plt.ylabel('Yield')
    plt.legend()
    plt.savefig('yield_curve_analysis.png')
    plt.close()

yield_curve_analysis()

def corporate_vs_treasury_analysis():
    # Plotting Baa and Aaa Corporate Bond Yields against 10-Year Treasury
    plt.figure(figsize=(12, 6))
    plt.plot(data_10_year, label='10-Year Treasury')
    plt.plot(data_baa_bond_yield, label="Baa Corporate Bond Yield")
    plt.plot(data_aaa_bond_yield, label="Aaa Corporate Bond Yield")
    plt.title('Corporate Bonds vs. Treasury Securities')
    plt.xlabel('Date')
    plt.ylabel('Yield')
    plt.legend()
    plt.savefig('corporate_vs_treasury.png')
    plt.close()

corporate_vs_treasury_analysis()

def federal_funds_rate_impact_analysis():
    plt.figure(figsize=(12, 6))
    plt.plot(data_10_year_minus_ffr, label='10-Year Treasury Minus Federal Funds Rate')
    plt.title('10-Year Treasury vs. Federal Funds Rate')
    plt.xlabel('Date')
    plt.ylabel('Rate Difference')
    plt.legend()
    plt.savefig('federal_funds_rate_impact.png')
    plt.close()

federal_funds_rate_impact_analysis()


def correlation_analysis():
    merged_data = pd.merge(data_10_year, data_baa_bond_yield, left_index=True, right_index=True, how='inner')
    correlation, _ = pearsonr(merged_data['Value_x'], merged_data['Value_y'])
    print(f'Correlation between 10-Year Treasury and Baa Corporate Bond Yield: {correlation}')

correlation_analysis()


def write_report():
    with open('analysis_report.md', 'w') as report:
        report.write("# Comprehensive Financial Market Analysis Report\n")
        report.write("## Introduction\n")
        report.write("This report provides an in-depth analysis of various financial market indicators...\n")
        # Individual dataset analysis
        report.write("## Yield Curve Analysis\n")
        report.write("![Yield Curve Analysis](yield_curve_analysis.png)\n")
        # Add interpretation of the yield curve analysis
        # Continue for other sections...
        report.write("## Conclusion\n")
        report.write("The findings suggest...")
        report.write("## References\n")
        report.write("1. [Financial Data](https://fred.stlouisfed.org/)\n")
        
        # Appendices with additional graphs and statistical analysis

write_report()



