import pyodbc

# Define your connection string
# Adjust the DRIVER name based on your ODBC driver
# conn_str = (
#     r'DRIVER=TallyODBC64_9001;'
#     r'SERVER=localhost;'
#     r'PORT=9001;'
#     r'TDS_Version=7.2;'
# )

conn_str = (r'DSN=TallyODBC64_9001;')

# Establish a connection to Tally via ODBC
# try:
conn = pyodbc.connect(conn_str, timeout=10)
print("Connected successfully to Tally ODBC Server")
    
#     # Create a cursor object using the connection
cursor = conn.cursor()
query = "SELECT * FROM LedgerVouchers"

# cursor.description returns column names once a query is executed for a table
    
#     # SQL query to fetch vouchers (adjust the query as per your requirement)
#     query = "SELECT * FROM Vouchers"

#     # Execute the query
#     cursor.execute(query)

#     # Fetch all rows
#     rows = cursor.fetchall()

#     # Iterate and print each row
#     for row in rows:
#         print(row)

# except Exception as e:
#     print("Error connecting to Tally ODBC Server:", e)

# finally:
#     if conn:
#         conn.close()

# print("Available Tables:")
# tables = cursor.tables()
# for table in tables:
#     print(table.table_name)