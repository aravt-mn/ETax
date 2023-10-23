import pandas as pd
import json

# Read the JSON data from a file into a string variable
with open('inventory_list.json', 'r', encoding='utf-8') as f:
    json_data = f.read()

# Load the JSON data into a pandas dataframe
data = json.loads(json_data)['data']
df = pd.json_normalize(data)

# Write the dataframe to a CSV file
df.to_csv('inventory_list.csv', index=False, encoding = 'utf-8-sig')