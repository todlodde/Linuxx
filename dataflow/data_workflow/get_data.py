from fredapi import Fred

fred = Fred(api_key='6c750bb903cb524f29be6d4926107f7e')

# Retrieve data for the 10-Year Treasury Constant Maturity Rate
data = fred.get_series('DGS10')

# Save data to a CSV file
data.to_csv('data.csv')
