import os
import pandas as pd
import zipfile

# code implementation to ...
# important link
# https://github.com/RobMulla/twitch-stream-projects/blob/main/050-flights/DataPrep.ipynb

# Define the directory
directory = 'D:\Trainee-Challenge\datasets'

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