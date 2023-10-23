import pandas as pd
import pyodbc

conn = pyodbc.connect('DRIVER={SQL Server};SERVER=172.31.0.116;DATABASE=Etax_test;UID=sa;PWD=UltSvr2k20@Apu')

# Read the data from the ultimate_inventory_list.csv file into a pandas dataframe
df1 = pd.read_csv('ultimate_inventory_list.csv')

# Insert the data from the ultimate_inventory_list.csv file into the ultimate_inventory_list table
cursor = conn.cursor()
for index, row in df1.iterrows():
    cursor.execute('INSERT INTO ultimate_inventory_list (isbn, invtID, descr, tranStatus) VALUES (?, ?, ?, ?)',
                   row['isbn'], row['invtID'], row['descr'], row['tranStatus'])
conn.commit()

# Read the data from the inventory_list.csv file into a pandas dataframe
# df2 = pd.read_csv('inventory_list.csv')

# # Insert the data from the inventory_list.csv file into the inventory_list table
# for index, row in df2.iterrows():
#     cursor.execute('INSERT INTO inventory_list (barcode, barcodeName, classificationCode, productTypeCode, productTypeName, productCategory, productPercent, productSize, unitCode) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)',
#                    row['barcode'], row['barcodeName'], row['classificationCode'], row['productTypeCode'], row['productTypeName'], row['productCategory'], row['productPercent'], row['productSize'], row['unitCode'])
# conn.commit()

# print('Data inserted successfully!')