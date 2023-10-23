import pandas as pd
import json

# Read the JSON data from a file into a string variable
with open('ultimate_inventory_list.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# Extract the 'isbn', 'invtID', 'descr', and 'tranStatus' values from the 'retdata' object
isbn_list = [item['isbn'] for item in data['retdata']['isbn']]
invtID_list = [item['invtID'] for item in data['retdata']['isbn']]
descr_list = [item['descr'] for item in data['retdata']['isbn']]
tranStatus_list = [item['tranStatus'] for item in data['retdata']['isbn']]

# Create a pandas dataframe with the extracted values
df = pd.DataFrame({'isbn': isbn_list, 'invtID': invtID_list, 'descr': descr_list, 'tranStatus': tranStatus_list})

# # Write the dataframe to a CSV file
df.to_csv('ultimate_inventory_list.csv', index=False, encoding = 'utf-8-sig')