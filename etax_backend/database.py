import pyodbc
import configparser

# Load database configuration from config.ini
config = configparser.ConfigParser()
config.read('config/config.ini')

server = config['DATABASE']['SERVER']
username = config['DATABASE']['USERNAME']
password = config['DATABASE']['PASSWORD']
db = config['DATABASE']['DATABASE']

CONN_STRING = f"Driver={{ODBC Driver 17 for SQL Server}};Server={server};Database={db};UID={username};PWD={password}"

def get_conn():
    return pyodbc.connect(CONN_STRING)