import pandas as pd
import os

data_folder = 'data'
files = ['daily_sales_data_0.csv', 'daily_sales_data_1.csv', 'daily_sales_data_2.csv'] 

all_data = []

for file in files:
    path = os.path.join(data_folder, file)
    df = pd.read_csv(path)

    # Filter for Pink Morsels only
    pink_df = df[df['product'] == 'pink morsel']
    
    # Remove '$' from price column and convert to float and ensure 'quantity' is numeric
    df['price'] = df['price'].replace('[\$,]', '', regex=True).astype(float)
    df['quantity'] = pd.to_numeric(df['quantity'], errors='coerce')
    
    # copy the dataframe before  filtering
    pink_df = df[df['product'].str.strip().str.lower() == 'pink morsel'].copy()
    
    #Create 'sales' column
    pink_df['sales'] = pink_df['quantity'] * pink_df['price']

    # Keep only 'sales', 'date', and 'region'
    formatted_df = pink_df[['sales', 'date', 'region']]

    all_data.append(formatted_df)

# Combine all datasets
final_df = pd.concat(all_data)

# Save to output CSV
output_path = os.path.join(data_folder, 'formatted_sales_data.csv')
final_df.to_csv(output_path, index=False)

