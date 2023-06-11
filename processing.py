import os
import pandas as pd
import zipfile

# data source: https://www.kaggle.com/datasets/divyansh22/flight-delay-prediction?select=Jan_2020_ontime.csv

# Define the directory
directory = 'D:\Trainee-Challenge\datasets'

def concat_data(dir):
    df_list= []
    # Traverse through the directory
    for filename in os.listdir(directory):
        if 'csv' not in filename:
            # Construct the full file path
            filepath = os.path.join(directory, filename)
            with zipfile.ZipFile(filepath, 'r') as zfiles:
                for name in zfiles.namelist():
                    if name.endswith('.csv'):
                        df = pd.read_csv(zfiles.open(name))
                        df_list.append(df)

        
    final_df = pd.concat(df_list)
    final_df.to_parquet('./datasets/final.parquet', engine='fastparquet')

concat_data(directory)

# air carrier names and codes data.

url = 'https://aspm.faa.gov/aspmhelp/index/ASQP__Carrier_Codes_and_Names.html'

def get_carrier_data(url):
    #the read_html method recieves the url as a parameter
    web_tables = pd.read_html(url)

    #let's read the first table on the webpage with index 0
    carrier_table = web_tables[0]
    carrier_table.to_csv('./datasets/carrier_table.csv')

get_carrier_data(url)


