import pyodbc
import json

# Connect to the SQL Server database
conn = pyodbc.connect('DRIVER={SQL Server};SERVER=172.31.0.116;DATABASE=Etax_test;UID=sa;PWD=UltSvr2k20@Apu')

# Load the JSON data from the file
with open('ultimate_inventory_list.json', 'r') as f:
    data = json.load(f)

# Extract the 'isbn', 'invtID', 'descr', and 'tranStatus' values from the JSON data
values = [(item['isbn'], item['invtID'], item['descr'], item['tranStatus']) for item in data['retdata']['isbn']]

# Define the SQL statement to insert the values into the ultimate_inventory_list table
insert_sql = 'INSERT INTO ultimate_inventory_list (isbn, invtID, descr, tranStatus) VALUES (?, ?, ?, ?)'

# Execute the SQL statement to insert the values into the ultimate_inventory_list table
cursor = conn.cursor()
cursor.executemany(insert_sql, values)
conn.commit()

print('Data inserted into ultimate_inventory_list table successfully!')