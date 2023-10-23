import datetime
import requests
import json
import pyodbc

def get_token():
    url = 'https://auth.itc.gov.mn/auth/realms/Staging/protocol/openid-connect/token'
    payload = {'client_id': 'e-inventory', 'grant_type': 'password', 'username': 'УШ00210275', 'password': 'Oyun1005'}
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}

    response = requests.post(url, data=payload, headers=headers)

    if response.status_code == 200:
        token = response.json()['access_token']
        return token
    else:
        return f"Error: {response.status_code} - {response.reason}"

def check_token():
    # Connect to the destination MSSQL server
    source_conn = pyodbc.connect('DRIVER={SQL Server};SERVER=172.31.0.116;DATABASE=Etax_test;UID=sa;PWD=UltSvr2k20@Apu')

    # Create a cursor for the source connection
    source_cursor = source_conn.cursor()

    # Execute the SQL query on the source server
    query = "select token, LOAD_DATETIME, tokenDuration from Etax.Token where Company="+"00074"
    source_cursor.execute(query)

    rows = source_cursor.fetchmany(1)

    ret = False
    token = rows[0][0]
    expires = rows[0][2]

    dtLoad = rows[0][1]

    if expires != None:
        maxDate = dtLoad + datetime.timedelta(seconds=expires) - datetime.timedelta(seconds=20)
        
        #print(maxDate)

        if maxDate > datetime.now():
            ret = True

    if ret == False:
        return get_token()
    
    return token

def get_inventory_list():
    url = 'https://service.itc.gov.mn/rest/tais-tpi-main-service/mainApi/getInventoryList'
    # headers = {'Authorization': f'Bearer {}'}

    params = {}

    response = requests.get(url, params=params)

    if response.status_code == 200:
        inventory_list = response.json()
        with open('response/inventory_list.json', 'w') as f:
            json.dump(inventory_list, f)

        # Connect to the SQL Server database
        conn = pyodbc.connect('DRIVER={SQL Server};SERVER=172.31.0.116;DATABASE=Etax_test;UID=sa;PWD=UltSvr2k20@Apu')

        # Create a cursor for the connection
        cursor = conn.cursor()

        # Insert the JSON data into the database
        for item in inventory_list['data']:
            cursor.execute('INSERT INTO inventory_list (barcode, barcodeName, classificationCode, productTypeCode, productTypeName, productCategory, productPercent, productSize, unitCode) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)',
                           item['barcode'], item['barcodeName'], item['classificationCode'], item['productTypeCode'], item['productTypeName'], item['productCategory'], item['productPercent'], item['productSize'], item['unitCode'])

        # Commit the changes to the database
        conn.commit()

        # Close the cursor and connection
        cursor.close()
        conn.close()

        return 1
    else:
        return f"Error: {response.status_code} - {response.reason}"
    
def get_active_stock_list(token):
    url = 'https://service.itc.gov.mn/api/inventory/getActiveStockNoPos/'
    headers = {'Authorization': f'Bearer {token}'}

    params = {
        ''
        "regNo": "2695456",
        "barCode": "69200110011",
        "stockType": "4",
        "positionId": "3",
        "year": "2023",
        "month": "10"
        ''
    }

    response = requests.get(url, headers=headers, params=params)

    if response.status_code == 200:
        active_stock_list = response.json()
        with open('response/active_stock_list.json', 'w') as f:
            json.dump(active_stock_list, f)
        return active_stock_list
    else:
        return f"Error: {response.status_code} - {response.reason}"
    
    
    
def main():
    # token = get_token()
    inventory_list = get_inventory_list()
    # print(inventory_list)
    # print(token)
    #token = get_token()
    # print(token)
    # active_stock_list = get_active_stock_list(token)
    # print(active_stock_list)
    # token = check_token()

if __name__ == '__main__':
    main()