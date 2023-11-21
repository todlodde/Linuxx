from fredapi import Fred

fred = Fred(api_key='6c750bb903cb524f29be6d4926107f7e')

# 10-Year Treasury Constant Maturity
data_10_year = fred.get_series('DGS10')
data_10_year.to_csv('data_10_year_treasury.csv')

# 10-Year Treasury Constant Maturity Minus 2-Year Treasury Constant Maturity
data_10_2_year = fred.get_series('T10Y2Y')
data_10_2_year.to_csv('data_10_2_year_spread.csv')

# 10-Year Treasury Constant Maturity Minus 3-Month Treasury Constant Maturity
data_10_3_month = fred.get_series('T10Y3M')
data_10_3_month.to_csv('data_10_3_month_spread.csv')

# Moody's Seasoned Baa Corporate Bond Yield Relative to Yield on 10-Year Treasury Constant Maturity
data_baa_bond_yield = fred.get_series('BAA10Y')
data_baa_bond_yield.to_csv('data_baa_corporate_bond_yield.csv')

# 10-Year Treasury Constant Maturity Minus Federal Funds Rate
data_10_year_minus_ffr = fred.get_series('T10YFF')
data_10_year_minus_ffr.to_csv('data_10_year_minus_fed_funds_rate.csv')

# Moody's Seasoned Aaa Corporate Bond Yield Relative to Yield on 10-Year Treasury Constant Maturity
data_aaa_bond_yield = fred.get_series('AAA10Y')
data_aaa_bond_yield.to_csv('data_aaa_corporate_bond_yield.csv')

