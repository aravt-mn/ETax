from flask import Flask,jsonify,request
from database import get_conn
import configparser
import requests
from datetime import datetime
import json

config = configparser.ConfigParser()
config.read('config/config.ini')

auth_url = config['API']['auth_url']
inventory_list_url = config['API']['inventory_list_url']
active_stock_url = config['API']['active_stock_url']
pos_set_transaction_url = config['API']['pos_set_transaction_url']

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecretkey'

users = [
    {'id': 1, 'username': 'aravt', 'password': 'Asuult12345'}
]

@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/api/products')
def get_products():
    # conn = get_conn()
    # cursor = conn.cursor()

    # cursor.execute('SELECT [ID] ,[SKU] ,[barcode] ,[itemName] ,[itemNameEn] ,[classificationCode] ,[productTypeCode] ,[productTypeName] ,[productCategory] ,[productPercent] ,[productSize] ,[unitCode] FROM [Etax_test].[ETax].[Items]')
    products = [
        {'id': 1, 'name': 'Product 1', 'price': 10.0},
        {'id': 2, 'name': 'Product 2', 'price': 20.0},
        {'id': 3, 'name': 'Product 3', 'price': 30.0},
    ]
    # cursor.close()
    # conn.close()
    return jsonify(products)

@app.route('/api/items')
def get_items():
    conn = get_conn()
    cursor = conn.cursor()
    
    cursor.execute('SELECT [ID], [SKU], [barcode], [itemName], [itemNameEn], [classificationCode], [productTypeCode], [productTypeName], [productCategory], [productPercent], [productSize], [unitCode] FROM [Etax_test].[ETax].[Items]')
    items = []
    for row in cursor.fetchall():
        items.append({
            'id': row[0],
            'SKU': row[1],
            'barcode': row[2],
            'itemName': row[3],
            'itemNameEn': row[4],
            'classificationCode': row[5],
            'productTypeCode': row[6],
            'productTypeName': row[7],
            'productCategory': row[8],
            'productPercent': row[9],
            'productSize': row[10],
            'unitCode': row[11]
        })
    
    cursor.close()
    conn.close()
    
    return jsonify(items)

@app.route('/api/producttypes')
def getproducttypes():
    conn = get_conn()
    cursor = conn.cursor()
    
    cursor.execute('SELECT [ID] ,[productTypeCode] ,[productTypeName] FROM [Etax_test].[ETax].[ProductTypes]')
    producttypes = []
    for row in cursor.fetchall():
        producttypes.append({
            'id': row[0],
            'productTypeCode': row[1],
            'productTypeName': row[2]
        })
    
    cursor.close()
    conn.close()
    
    return jsonify(producttypes)

@app.route('/api/inventorylist/<int:page_num>')
def inventorylist(page_num):
    conn = get_conn()
    cursor = conn.cursor()
    
    page_size = 10 # Change this to the desired page size
    offset = (page_num - 1) * page_size
    
    cursor.execute('SELECT [ID], [barcode], [barcodeName], [classificationCode], [productTypeCode], [productTypeName], [productCategory], [productPercent], [productSize], [unitCode], [LOAD_DATETIME] FROM [Etax_test].[ETax].[InventoryList] ORDER BY [ID] OFFSET ? ROWS FETCH NEXT ? ROWS ONLY', offset, page_size)
    
    inventorylist = []
    for row in cursor.fetchall():
        inventorylist.append({
            'id': row[0],
            'barcode': row[1],
            'barcodeName': row[2],
            'classificationCode': row[3],
            'productTypeCode': row[4],
            'productTypeName': row[5],
            'productCategory': row[6],
            'productPercent': row[7],
            'productSize': row[8],
            'unitCode': row[9],
            'loaddatetime': row[10]
        })
    
    cursor.close()
    conn.close()
    
    return jsonify(inventorylist)

# refresh inventory_list_url data
@app.route('/api/inventorylist/refresh')
def refresh_inventorylist():
    params = {}

    response = requests.get(inventory_list_url, params=params)

    if response.status_code == 200:
        inventory_list = response.json()
        now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
        filename = f'../response/inventory_list_{now}.json'
        with open(filename, 'w') as f:
            json.dump(inventory_list, f)

        # Connect to the SQL Server database
        conn = get_conn()

        # Create a cursor for the connection
        cursor = conn.cursor()

        # Delete the existing data from the InventoryList table
        cursor.execute('DELETE FROM [ETax].[InventoryList]')

        # Insert the JSON data into the database
        for item in inventory_list['data']:
            cursor.execute('INSERT INTO [ETax].[InventoryList] (barcode, barcodeName, classificationCode, productTypeCode, productTypeName, productCategory, productPercent, productSize, unitCode) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)',
                           item['barcode'], item['barcodeName'], item['classificationCode'], item['productTypeCode'], item['productTypeName'], item['productCategory'], item['productPercent'], item['productSize'], item['unitCode'])

        # Commit the changes to the database
        conn.commit()

        # Close the cursor and connection
        cursor.close()
        conn.close()

        return 'Inventory list refreshed successfully'
    else:
        return f"Error: {response.status_code} - {response.reason}"


@app.route('/login', methods=['POST'])
def login():
    username = request.json.get('username')
    password = request.json.get('password')
    user = next((user for user in users if user['username'] == username and user['password'] == password), None)
    if user:
        # token = jwt.encode({'id': user['id']}, app.config['SECRET_KEY'])
        return jsonify({'token': '12312312'})
    else:
        return jsonify({'error': 'Invalid username or password'}), 401