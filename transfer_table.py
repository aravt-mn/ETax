import pyodbc
from tqdm import tqdm

# Connect to the source MSSQL server
source_conn = pyodbc.connect('DRIVER={SQL Server};SERVER=172.31.0.121;DATABASE=StagingMemory;UID=sa-dwh;PWD=KxGQ35Wq0e*@')

# Connect to the destination MSSQL server
dest_conn = pyodbc.connect('DRIVER={SQL Server};SERVER=172.31.0.116;DATABASE=Etax_test;UID=sa;PWD=UltSvr2k20@Apu')

# Create a cursor for the source connection
source_cursor = source_conn.cursor()

# Execute the SQL query on the source server
query = "select [SDKCOO] ,[SDDOCO] ,[SDDCTO] ,[SDLNID] ,[SDOGNO] ,[SDAN8] ,[SDSHAN] ,[SDPA8] ,[SDDRQJ] ,[SDDGL] ,[SDITM] ,[SDLITM] ,[SDLOCN] ,[SDDSC1] ,[SDDSC2] ,[SDLNTY] ,[SDBCRC] ,[SDNXTR] ,[SDLTTR] ,[SDEMCU] ,[SDSRP5] ,[SDUOM1] ,[SDSOQS] ,[SDUPRC] ,[SDUORG] ,[SDAEXP] ,[SDUNCS] ,[SDECST] ,[SDTXA1] ,[SDEXR1] ,[SDGLC] from jde.F42119 with (nolock) where sdkcoo in ('00011', '00018', '00097') and sddgl>=apu_dw.dbo.dmytojul(getdate())-40 and RowActiveIndicator='Y'"
source_cursor.execute(query)

# Define the batch size
batch_size = 5000

# Create a cursor for the destination connection
dest_cursor = dest_conn.cursor()

# Insert the rows into the destination table in batches
with tqdm(total=source_cursor.rowcount) as pbar:
    while True:
        rows = source_cursor.fetchmany(batch_size)
        if not rows:
            break
        dest_cursor.executemany('INSERT INTO F42119 ([SDKCOO] ,[SDDOCO] ,[SDDCTO] ,[SDLNID] ,[SDOGNO] ,[SDAN8] ,[SDSHAN] ,[SDPA8] ,[SDDRQJ] ,[SDDGL] ,[SDITM] ,[SDLITM] ,[SDLOCN] ,[SDDSC1] ,[SDDSC2] ,[SDLNTY] ,[SDBCRC] ,[SDNXTR] ,[SDLTTR] ,[SDEMCU] ,[SDSRP5] ,[SDUOM1] ,[SDSOQS] ,[SDUPRC] ,[SDUORG] ,[SDAEXP] ,[SDUNCS] ,[SDECST] ,[SDTXA1] ,[SDEXR1] ,[SDGLC]) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?,?,?,?,?,?)', rows)
        pbar.update(len(rows))

# Commit the changes to the destination database
dest_conn.commit()

# Close the cursors and connections
source_cursor.close()
source_conn.close()
dest_cursor.close()
dest_conn.close()