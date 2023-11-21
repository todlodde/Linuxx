import pandas as pd

def transform_data(file_name):
    data = pd.read_csv(file_name, header=None, names=['Date', 'Value'])

    data.dropna(inplace=True) 
    data['Date'] = pd.to_datetime(data['Date']).dt.strftime('%Y-%m-%d')  

    transformed_file_name = f'transformed_{file_name}'
    data.to_csv(transformed_file_name, index=False)

datasets = ['data_10_year_treasury.csv', 'data_10_2_year_spread.csv', 
            'data_10_3_month_spread.csv', 'data_baa_corporate_bond_yield.csv',
            'data_10_year_minus_fed_funds_rate.csv', 'data_aaa_corporate_bond_yield.csv']

for dataset in datasets:
    transform_data(dataset)

